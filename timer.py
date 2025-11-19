import os
import json
import tkinter as tk
from tkinter import messagebox, ttk
from pathlib import Path
from PIL import Image, ImageTk

# pygame is optional but recommended for audio playback
try:
    import pygame
    PYGAME_AVAILABLE = True
except Exception:
    PYGAME_AVAILABLE = False

DATA_FILE = Path("hydration.json")
IMAGES_DIR = Path("images")


def load_state():
    """Load persisted count and goal (if exists)."""
    if DATA_FILE.exists():
        try:
            with open(DATA_FILE, "r", encoding="utf-8") as f:
                d = json.load(f)
            # reset count if date changed is not implemented here to keep simple
            return d.get("count", 0), d.get("goal", 8)
        except Exception:
            return 0, 8
    return 0, 8


def save_state(count, goal):
    try:
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump({"count": count, "goal": goal}, f)
    except Exception as e:
        print("Could not save state:", e)


class WaterReminderTimer:
    def __init__(self, root):
        self.root = root
        self.root.title("Hydration Timer")
        self.root.geometry("560x900")
        self.root.resizable(True, True)
        self.root.configure(bg="#0d1b2a")

        # load persisted state
        cnt, goal = load_state()
        self.water_count = cnt
        self.daily_goal = goal

        # Timer settings (default 10 sec for quick testing)
        self.total_time = 10
        self.remaining_time = self.total_time
        self.is_running = False

        # Alarm path (looks for alarm.mp3 or alarm.wav next to this script)
        self.alarm_path = self._find_alarm_file()

        # Initialize pygame mixer safely if available
        if PYGAME_AVAILABLE:
            try:
                pygame.mixer.init()
            except Exception as e:
                print("pygame mixer init warning:", e)

        # Load images (robust)
        self.images = self.load_images()

        # UI Elements
        self.create_widgets()

        # Keyboard bindings
        self.root.bind("<Escape>", lambda e: self.reset_timer())
        self.root.bind("<space>", lambda e: self.toggle_timer())
        self.root.bind("d", lambda e: self._manual_log())

        # update visuals
        self.update_visual()

    def _find_alarm_file(self):
        base = os.path.dirname(__file__)
        mp3 = os.path.join(base, "alarm.mp3")
        wav = os.path.join(base, "alarm.wav")
        if os.path.exists(mp3):
            return mp3
        if os.path.exists(wav):
            return wav
        return None

    def load_images(self):
        images = []
        # compatibility for Pillow resampling
        try:
            resample_mode = Image.Resampling.NEAREST
        except Exception:
            resample_mode = Image.NEAREST

        # expected names
        names = [f"full{i}.png" for i in range(7)]
        # fallback also tries "full.png" as first frame
        names_alt = ["full.png"] + [f"full{i}.png" for i in range(1, 7)]

        chosen = None
        # try both naming schemes
        if IMAGES_DIR.exists():
            if all((IMAGES_DIR / n).exists() for n in names):
                chosen = names
            elif all((IMAGES_DIR / n).exists() for n in names_alt):
                chosen = names_alt

        if chosen:
            for name in chosen:
                try:
                    img = Image.open(IMAGES_DIR / name).convert("RGBA")
                    img = img.resize((180, 240), resample_mode)
                except Exception:
                    img = Image.new("RGBA", (180, 240), (255, 255, 255, 20))
                images.append(ImageTk.PhotoImage(img))
        else:
            # create placeholders
            for i in range(7):
                img = Image.new("RGBA", (180, 240), (15, 27, 42, 255))
                # simple level rectangle
                from PIL import ImageDraw
                d = ImageDraw.Draw(img)
                margin = 16
                level = int((i / 6.0) * (240 - 60))
                d.rounded_rectangle((margin, 16, 180 - margin, 240 - 16), radius=18, fill=(255, 255, 255, 10))
                d.rectangle((margin + 8, 240 - 24 - level, 180 - margin - 8, 240 - 24), fill=(60, 160, 255, 220))
                images.append(ImageTk.PhotoImage(img))
        # ensure length 7
        while len(images) < 7:
            images.append(images[-1])
        return images

    def create_widgets(self):
        main = tk.Frame(self.root, bg="#0d1b2a")
        main.pack(expand=True, fill="both", padx=20, pady=20)

        title = tk.Label(main, text="Hydration Timer", font=("Arima Madurai", 36, "bold"),
                         fg="#4dd0e1", bg="#0d1b2a")
        title.pack(pady=(0, 6))

        subtitle = tk.Label(main, text="Stay healthy — drink water regularly", font=("TkDefaultFont", 11),
                            fg="#90a4ae", bg="#0d1b2a")
        subtitle.pack(pady=(0, 12))

        # image
        self.img_label = tk.Label(main, image=self.images[0], bg="#0d1b2a")
        self.img_label.pack(pady=6)

        # timer display
        self.timer_var = tk.StringVar(value=self.format_time(self.remaining_time))
        self.timer_label = tk.Label(main, textvariable=self.timer_var, font=("TkDefaultFont", 56, "bold"),
                                    fg="#4dd0e1", bg="#0d1b2a")
        self.timer_label.pack(pady=8)

        # Controls row (Start / Reset / Log)
        controls = tk.Frame(main, bg="#0d1b2a")
        controls.pack(pady=8)

        self.start_btn = tk.Button(controls, text="START", command=self.toggle_timer,
                                   font=("Arial", 14, "bold"), bg="#4dd0e1", fg="#000000",
                                   width=16, height=2, bd=0, cursor="hand2")
        self.start_btn.grid(row=0, column=0, padx=6)

        self.reset_btn = tk.Button(controls, text="RESET", command=self.reset_timer,
                                   font=("Arial", 14, "bold"), bg="#ffa726", fg="#0d1b2a",
                                   width=10, height=2, bd=0, cursor="hand2")
        self.reset_btn.grid(row=0, column=1, padx=6)

        self.log_btn = tk.Button(controls, text="I DRANK (LOG)", command=self._manual_log,
                                 font=("Arial", 12, "bold"), bg="#7c4dff", fg="white",
                                 width=14, height=2, bd=0, cursor="hand2")
        self.log_btn.grid(row=0, column=2, padx=6)

        # Settings: Minutes and Goal
        settings = tk.Frame(main, bg="#0d1b2a")
        settings.pack(pady=10)

        # Minutes
        tk.Label(settings, text="Minutes:", fg="#90a4ae", bg="#0d1b2a").grid(row=0, column=0, padx=6)
        self.minutes_var = tk.IntVar(value=1)  # default 1 minute for dev/testing
        self.minutes_spin = ttk.Spinbox(settings, from_=1, to=180, textvariable=self.minutes_var, width=6)
        self.minutes_spin.grid(row=0, column=1, padx=6)
        apply_min_btn = tk.Button(settings, text="Apply", command=self.apply_minutes, bg="#2a9d8f", fg="white", bd=0, cursor="hand2")
        apply_min_btn.grid(row=0, column=2, padx=6)

        # Daily goal
        tk.Label(settings, text="Daily goal (glasses):", fg="#90a4ae", bg="#0d1b2a").grid(row=1, column=0, padx=6, pady=(8,0))
        self.goal_var = tk.IntVar(value=self.daily_goal)
        self.goal_spin = ttk.Spinbox(settings, from_=1, to=20, textvariable=self.goal_var, width=6)
        self.goal_spin.grid(row=1, column=1, padx=6, pady=(8,0))
        apply_goal_btn = tk.Button(settings, text="Set Goal", command=self.apply_goal, bg="#2a9d8f", fg="white", bd=0, cursor="hand2")
        apply_goal_btn.grid(row=1, column=2, padx=6, pady=(8,0))

        # Progress & counts
        card = tk.Frame(main, bg="#1a2f45", padx=12, pady=10)
        card.pack(pady=12, fill="x", padx=8)
        tk.Label(card, text="💧", font=("TkDefaultFont", 28), bg="#1a2f45").pack(side="left", padx=10)
        info = tk.Frame(card, bg="#1a2f45")
        info.pack(side="left")
        tk.Label(info, text="Glasses today", fg="#90a4ae", bg="#1a2f45").pack(anchor="w")
        self.count_var = tk.IntVar(value=self.water_count)
        tk.Label(info, textvariable=self.count_var, font=("TkDefaultFont", 28, "bold"), fg="#4dd0e1", bg="#1a2f45").pack(anchor="w")

        # Progress bar for goal
        self.progress = ttk.Progressbar(main, maximum=100, length=480)
        self.progress.pack(pady=(8, 6))

        # Status label
        self.status_label = tk.Label(main, text="Ready to start", font=("TkDefaultFont", 12), fg="#90a4ae", bg="#0d1b2a")
        self.status_label.pack(pady=6)

    def format_time(self, seconds):
        minutes = seconds // 60
        secs = seconds % 60
        return f"{minutes:02d}:{secs:02d}"

    def apply_minutes(self):
        mins = int(self.minutes_var.get())
        if mins <= 0:
            messagebox.showwarning("Invalid", "Please enter a positive minute value.")
            return
        self.total_time = mins * 60
        self.remaining_time = self.total_time
        self.status_label.config(text=f"Timer set to {mins} minute(s)", fg="#90a4ae")
        self.update_visual()

    def apply_goal(self):
        goal = int(self.goal_var.get())
        if goal <= 0:
            messagebox.showwarning("Invalid", "Goal must be at least 1.")
            return
        self.daily_goal = goal
        save_state(self.water_count, self.daily_goal)
        self.status_label.config(text=f"Goal set to {goal} glasses", fg="#90a4ae")
        self.update_visual()

    def get_current_image_index(self):
        if self.total_time <= 0:
            return 0
        progress = (self.total_time - self.remaining_time) / float(self.total_time)
        idx = int(progress * 6)
        return max(0, min(6, idx))

    def update_visual(self):
        # image
        idx = self.get_current_image_index()
        try:
            self.img_label.config(image=self.images[idx])
            self.img_label.image = self.images[idx]
        except Exception:
            pass
        # time text
        self.timer_var.set(self.format_time(self.remaining_time))
        # count & progress
        self.count_var.set(self.water_count)
        percent = int((self.water_count / max(1, self.daily_goal)) * 100)
        percent = min(100, percent)
        self.progress['value'] = percent

    def toggle_timer(self):
        if self.is_running:
            self.is_running = False
            self.start_btn.config(text="RESUME", bg="#4dd0e1", fg="#000000")
            self.status_label.config(text="Paused", fg="#ffa726")
        else:
            self.is_running = True
            # ensure total_time uses applied minutes if any
            if getattr(self, "total_time", None) is None:
                self.total_time = 10
            if self.remaining_time <= 0:
                self.remaining_time = self.total_time
            self.start_btn.config(text="PAUSE", bg="#4dd0e1", fg="#000000")
            self.status_label.config(text="Timer active!", fg="#4dd0e1")
            self._tick()

    def _tick(self):
        if not self.is_running:
            return
        if self.remaining_time > 0:
            self.remaining_time -= 1
            self.update_visual()
            self.root.after(1000, self._tick)
        else:
            self.timer_complete()

    def timer_complete(self):
        self.is_running = False
        self.water_count += 1
        self.count_var.set(self.water_count)
        save_state(self.water_count, self.daily_goal)

        # Play alarm (loop until user clicks OK)
        if self.alarm_path:
            self.play_alarm()
        else:
            print("No alarm file found; place alarm.mp3 or alarm.wav in the folder.")

        # Show notification (blocks until OK is clicked)
        messagebox.showinfo(
            "Time to Hydrate!",
            "Time to drink a glass of water!\n\nClick OK when done."
        )

        # Stop alarm when OK is clicked
        if PYGAME_AVAILABLE:
            try:
                pygame.mixer.music.stop()
            except Exception:
                pass

        # Reset timer for next round
        self.remaining_time = self.total_time
        self.update_visual()
        self.start_btn.config(text="START", bg="#1a2b45", fg="white")
        self.status_label.config(text="Great job!", fg="#4caf50")

    def play_alarm(self):
        """Play alarm sound (loops until stopped by user clicking OK)."""
        try:
            if self.alarm_path and os.path.exists(self.alarm_path):
                if PYGAME_AVAILABLE:
                    try:
                        pygame.mixer.music.load(self.alarm_path)
                        pygame.mixer.music.play(-1)  # loop indefinitely
                    except Exception as e:
                        print("pygame error while playing:", e)
                else:
                    # fallback for wav on Windows
                    if self.alarm_path.lower().endswith(".wav"):
                        try:
                            import platform
                            if platform.system() == "Windows":
                                import winsound
                                winsound.PlaySound(self.alarm_path, winsound.SND_FILENAME | winsound.SND_ASYNC)
                            else:
                                os.system(f"aplay \"{self.alarm_path}\" &")
                        except Exception as e:
                            print("Fallback wav play error:", e)
                    else:
                        print("No pygame available to play mp3. Install pygame for audio support.")
            else:
                print("Alarm file not found:", self.alarm_path)
        except Exception as e:
            print(f"Could not play alarm: {e}")

    def reset_timer(self):
        self.is_running = False
        self.remaining_time = self.total_time
        self.update_visual()
        self.start_btn.config(text="START", bg="#ffa726", fg="white")
        self.status_label.config(text="Timer reset", fg="#90a4ae")
        # stop alarm if playing
        if PYGAME_AVAILABLE:
            try:
                pygame.mixer.music.stop()
            except Exception:
                pass

    def _manual_log(self):
        self.water_count += 1
        save_state(self.water_count, self.daily_goal)
        self.update_visual()
        self.status_label.config(text="Logged a glass (manual).", fg="#4dd0e1")


def main():
    IMAGES_DIR.mkdir(exist_ok=True)
    root = tk.Tk()
    app = WaterReminderTimer(root)
    root.mainloop()


if __name__ == "__main__":
    main()
