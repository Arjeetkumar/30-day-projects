import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk, UnidentifiedImageError
import os
import json
import random
import shutil
import time
import zipfile
import threading

try:
    import pygame
    PYGAME_AVAILABLE = True
except Exception:
    PYGAME_AVAILABLE = False

APP_NAME = "Daily Motivation Affirmations"
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IMAGES_DIR = os.path.join(BASE_DIR, "images")
FAV_DIR = os.path.join(BASE_DIR, "favorites")
SETTINGS_PATH = os.path.join(BASE_DIR, "settings.json")
CAPTIONS_PATH = os.path.join(BASE_DIR, "captions.txt")
SOUND_PATH = os.path.join(BASE_DIR, "sound.mp3")  # optional

DEFAULT_SETTINGS = {
    "interval": 3,          # seconds per image
    "shuffle": True,
    "last_index": 0,
    "scale_mode": "fit"     # could expand to 'fill'
}

SUPPORTED_EXT = (".png", ".jpg", ".jpeg", ".gif", ".bmp", ".webp")

# ----------------------------
# Utility functions
# ----------------------------
def ensure_dirs():
    os.makedirs(IMAGES_DIR, exist_ok=True)
    os.makedirs(FAV_DIR, exist_ok=True)

def load_settings():
    if os.path.exists(SETTINGS_PATH):
        try:
            with open(SETTINGS_PATH, "r", encoding="utf-8") as f:
                data = json.load(f)
                s = DEFAULT_SETTINGS.copy()
                s.update({k: data.get(k, s[k]) for k in s})
                return s
        except Exception:
            pass
    return DEFAULT_SETTINGS.copy()

def save_settings(s):
    try:
        with open(SETTINGS_PATH, "w", encoding="utf-8") as f:
            json.dump(s, f, indent=2)
    except Exception as e:
        print("Could not save settings:", e)

def find_images(folder):
    images = []
    for root, _, files in os.walk(folder):
        for fn in sorted(files):
            if fn.lower().endswith(SUPPORTED_EXT):
                images.append(os.path.join(root, fn))
    return images

def read_captions():
    # captions.txt may contain lines "filename|caption" or just "caption"
    if not os.path.exists(CAPTIONS_PATH):
        return {}
    out = {}
    try:
        with open(CAPTIONS_PATH, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line: continue
                if "|" in line:
                    a, b = line.split("|", 1)
                    out[a.strip()] = b.strip()
                else:
                    out.setdefault("__pool__", []).append(line)
    except Exception:
        pass
    return out

# ----------------------------
# App Class
# ----------------------------
class AffirmationApp:
    def __init__(self, root):
        ensure_dirs()
        self.root = root
        self.root.title(APP_NAME)
        self.root.geometry("900x600")
        self.root.minsize(420, 300)
        self.root.configure(bg="#0b1220")

        # Load settings and assets
        self.settings = load_settings()
        self.images = find_images(IMAGES_DIR)
        self.captions = read_captions()
        self.index_list = list(range(len(self.images)))
        if self.settings.get("shuffle"):
            random.shuffle(self.index_list)

        self.current_pos = 0
        # if setting remembered, try to position near that
        last_idx = self.settings.get("last_index", 0)
        if 0 <= last_idx < len(self.images):
            try:
                self.current_pos = self.index_list.index(last_idx)
            except Exception:
                self.current_pos = 0

        # playback state
        self.is_playing = True
        self._timer_job = None
        self._last_change = time.time()

        # profile points / extras (persist in settings): simple points for viewing
        self.profile = self.settings.get("profile", {"points": 0, "level": 1})

        # optional sound init
        if PYGAME_AVAILABLE and os.path.exists(SOUND_PATH):
            try:
                pygame.mixer.init()
                pygame.mixer.music.load(SOUND_PATH)
            except Exception as e:
                print("pygame sound error:", e)

        # UI elements
        self.build_ui()

        # start slideshow if images exist; else show placeholder
        if not self.images:
            self.show_empty_state()
        else:
            self.show_image_at(0, force=True)
            if self.is_playing:
                self.schedule_next()

        # keyboard bindings
        self.root.bind("<space>", lambda e: self.toggle_play())
        self.root.bind("<Right>", lambda e: self.next_image())
        self.root.bind("<Left>", lambda e: self.prev_image())
        self.root.bind("s", lambda e: self.toggle_shuffle())
        self.root.bind("f", lambda e: self.toggle_fullscreen())
        self.root.bind("+", lambda e: self.change_interval(1))
        self.root.bind("-", lambda e: self.change_interval(-1))
        self.root.bind("n", lambda e: self.import_images())
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)

    # ---------------- UI ----------------
    def build_ui(self):
        # top frame: controls + profile
        top = tk.Frame(self.root, bg="#0b1220")
        top.pack(side="top", fill="x", padx=12, pady=(10,6))

        # left controls
        ctrl = tk.Frame(top, bg="#0b1220")
        ctrl.pack(side="left", anchor="w")

        self.btn_prev = self._tbtn(ctrl, "⟨ Prev", self.prev_image)
        self.btn_play = self._tbtn(ctrl, "Pause" if self.is_playing else "Play", self.toggle_play)
        self.btn_next = self._tbtn(ctrl, "Next ⟩", self.next_image)
        self.btn_shuffle = self._tbtn(ctrl, "Shuffle: ON" if self.settings.get("shuffle") else "Shuffle: OFF", self.toggle_shuffle)
        self.btn_full = self._tbtn(ctrl, "Fullscreen (F)", self.toggle_fullscreen)
        self.btn_fav = self._tbtn(ctrl, "★ Favorite", self.mark_favorite)
        self.btn_add = self._tbtn(ctrl, "➕ Add Images", self.import_images)

        # right profile area
        profile = tk.Frame(top, bg="#0b1220")
        profile.pack(side="right", anchor="e")
        self.points_label = tk.Label(profile, text=f"Points: {self.profile.get('points',0)}", fg="#00ff88", bg="#0b1220", font=("Inter", 10, "bold"))
        self.points_label.pack(anchor="e")
        self.level_label = tk.Label(profile, text=f"Level: {self.profile.get('level',1)}", fg="#00d4ff", bg="#0b1220", font=("Inter", 9))
        self.level_label.pack(anchor="e")

        # main display
        self.display = tk.Frame(self.root, bg="#f6f8fb", relief="flat", bd=0, highlightthickness=0)
        self.display.pack(expand=True, fill="both", padx=0, pady=0)

        # canvas for image display
        self.canvas = tk.Canvas(self.display, bg="#0a1828", highlightthickness=0, highlightcolor="#0a1828", relief="flat", bd=0)
        self.canvas.pack(expand=True, fill="both")
        self.canvas.bind("<Configure>", lambda e: self._on_canvas_resize())

        # caption overlay
        self.caption_var = tk.StringVar(value="")
        self.caption_label = tk.Label(self.canvas, textvariable=self.caption_var, bg="#1a2a3a", fg="#00ff88",
                                      font=("Inter", 14, "bold"), wraplength=700, justify="center", relief="flat", bd=0)
        # use place to overlay on canvas; we will update placement on resize
        self.caption_label.place_forget()

        # bottom controls + progress
        bottom = tk.Frame(self.root, bg="#0b1220", relief="flat", bd=0, highlightthickness=0)
        bottom.pack(side="bottom", fill="x", padx=12, pady=(6,12))

        # interval control
        self.interval_var = tk.IntVar(value=self.settings.get("interval", 3))
        tk.Label(bottom, text="Interval (s):", bg="#0b1220", fg="#00d4ff").pack(side="left", padx=(6,0))
        self.interval_entry = tk.Entry(bottom, textvariable=self.interval_var, width=4, bg="#1a2a3a", fg="#00ff88", insertbackground="#00ff88")
        self.interval_entry.pack(side="left", padx=(4,10))
        self.interval_entry.bind("<Return>", lambda e: self._interval_changed())

        # progress indicator (dots)
        self.progress_frame = tk.Frame(bottom, bg="#0b1220")
        self.progress_frame.pack(side="right", padx=6)
        self._render_progress_dots()

        # status label
        self.status_var = tk.StringVar(value="Ready")
        self.status = tk.Label(bottom, textvariable=self.status_var, bg="#0b1220", fg="#00d4ff")
        self.status.pack(side="left", padx=12)

    def _tbtn(self, parent, text, cmd):
        b = tk.Button(parent, text=text, command=cmd, bg="#1a3a4a", fg="#00ff88", bd=0, padx=8, pady=6, activebackground="#00ff88", activeforeground="#0b1220")
        b.pack(side="left", padx=6)
        return b

    # ---------------- image loading/resizing ----------------
    def _on_canvas_resize(self):
        # when canvas resizes, redraw current image
        self._update_image_on_canvas()

    def _update_image_on_canvas(self):
        # draw currently loaded PIL image (if any) scaled to canvas
        if not hasattr(self, "_current_pil") or self._current_pil is None:
            return
        cw = self.canvas.winfo_width()
        ch = self.canvas.winfo_height()
        if cw <= 10 or ch <= 10:
            return

        pil = self._current_pil.copy()
        # scale to fit while preserving aspect ratio
        w, h = pil.size
        # compute scale
        scale = min(cw / w, ch / h)
        new_w, new_h = int(w * scale), int(h * scale)
        try:
            pil = pil.resize((new_w, new_h), Image.LANCZOS)
        except Exception:
            pil = pil.resize((new_w, new_h))
        self._photo = ImageTk.PhotoImage(pil)  # keep reference
        self.canvas.delete("IMG")
        # center image on canvas
        self.canvas.create_image(cw//2, ch//2, image=self._photo, tags="IMG")
        # place caption label in bottom center of canvas
        cx = cw//2
        cy = ch - (new_h//2) - 40
        self.caption_label.place(x= max(20, cx- (min(700, new_w)//2)), y=cy, width=min(700, new_w))
        # update progress indicator highlight
        self._highlight_progress_dot()

    def _render_progress_dots(self):
        # create a set of small dots representing up to 20 images (cap)
        for widget in self.progress_frame.winfo_children():
            widget.destroy()
        total = min(20, len(self.images))
        for i in range(total):
            dot = tk.Canvas(self.progress_frame, width=8, height=8, bg="#0b1220", highlightthickness=0)
            dot.create_oval(1,1,7,7, fill="#274050", outline="")
            dot.pack(side="left", padx=2)
        self._highlight_progress_dot()

    def _highlight_progress_dot(self):
        total = min(20, len(self.images))
        if total == 0:
            return
        pos = 0
        if self.images:
            real_index = self.index_list[self.current_pos] if self.current_pos < len(self.index_list) else 0
            # map real_index to [0, total)
            pos = (self.current_pos % total) if total>0 else 0
        for i, child in enumerate(self.progress_frame.winfo_children()):
            child.delete("all")
            col = "#00ff88" if i == pos else "#0a4a5a"
            child.create_oval(1,1,7,7, fill=col, outline="")

    # ---------------- slideshow control ----------------
    def schedule_next(self):
        self.cancel_timer()
        interval = max(1, int(self.interval_var.get()))
        self._timer_job = self.root.after(interval * 1000, self._on_timer_tick)
        self.status_var.set(f"Next in {interval}s")

    def cancel_timer(self):
        if self._timer_job:
            try:
                self.root.after_cancel(self._timer_job)
            except Exception:
                pass
            self._timer_job = None

    def _on_timer_tick(self):
        # auto-advance if playing
        self._last_change = time.time()
        if self.is_playing:
            self.next_image()
            self.schedule_next()

    def toggle_play(self):
        self.is_playing = not self.is_playing
        self.btn_play.config(text="Pause" if self.is_playing else "Play")
        if self.is_playing:
            self.schedule_next()
        else:
            self.cancel_timer()
            self.status_var.set("Paused")

    def change_interval(self, delta):
        val = max(1, int(self.interval_var.get()) + int(delta)
)
        self.interval_var.set(val)
        self._interval_changed()

    def _interval_changed(self):
        # save new interval
        ival = max(1, int(self.interval_var.get()))
        self.settings["interval"] = ival
        save_settings(self.settings)
        self.status_var.set(f"Interval set to {ival}s")
        if self.is_playing:
            self.schedule_next()

    def toggle_shuffle(self):
        # toggle shuffle and rebuild index_list
        self.settings["shuffle"] = not self.settings.get("shuffle", False)
        self.btn_shuffle.config(text="Shuffle: ON" if self.settings["shuffle"] else "Shuffle: OFF")
        # rebuild index list while keeping current image
        current_real = self.index_list[self.current_pos] if self.images and 0 <= self.current_pos < len(self.index_list) else None
        self.index_list = list(range(len(self.images)))
        if self.settings["shuffle"]:
            random.shuffle(self.index_list)
        # try to set current_pos to current_real
        if current_real is not None and current_real in self.index_list:
            self.current_pos = self.index_list.index(current_real)
        else:
            self.current_pos = 0
        save_settings(self.settings)
        self._render_progress_dots()
        self.show_image_at(self.current_pos, force=True)

    def next_image(self):
        if not self.images: return
        self.current_pos = (self.current_pos + 1) % len(self.index_list)
        self.show_image_at(self.current_pos)
        # award small passive points for viewing
        self._award_points(1)

    def prev_image(self):
        if not self.images: return
        self.current_pos = (self.current_pos - 1) % len(self.index_list)
        self.show_image_at(self.current_pos)

    def show_empty_state(self):
        self.canvas.delete("all")
        self.caption_label.place_forget()
        self.canvas.create_text(self.canvas.winfo_width()//2 or 450, (self.canvas.winfo_height()//2) or 200,
                                text="No images found in ./images/\nClick 'Add Images' to select images.",
                                fill="#9fb6bd", font=("Inter", 18), justify="center")

    def show_image_at(self, pos, force=False):
        # pos is index into index_list
        if not self.images:
            self.show_empty_state()
            return
        pos = pos % len(self.index_list)
        real_index = self.index_list[pos]
        path = self.images[real_index] if real_index < len(self.images) else None
        if not path or not os.path.exists(path):
            # remove missing and re-run
            try:
                self.images = find_images(IMAGES_DIR)
                self.index_list = list(range(len(self.images)))
                if self.settings.get("shuffle"): random.shuffle(self.index_list)
                save_settings(self.settings)
            except Exception:
                pass
            self.status_var.set("Image missing — refreshed list")
            return

        # load the image via Pillow (handle errors)
        try:
            pil = Image.open(path).convert("RGBA")
        except UnidentifiedImageError:
            self.status_var.set("Could not open image (skipping).")
            # mark as removed
            try:
                self.images.pop(real_index)
                self.index_list = list(range(len(self.images)))
            except Exception:
                pass
            return
        except Exception as e:
            self.status_var.set(f"Error loading image: {e}")
            return

        self._current_pil = pil
        self._current_path = path
        self._current_real_index = real_index
        # set caption from captions.txt if available, else random from pool if present
        base = os.path.basename(path)
        caption = ""
        if base in self.captions:
            caption = self.captions[base]
        elif "__pool__" in self.captions:
            caption = random.choice(self.captions["__pool__"])
        else:
            caption = ""
        self.caption_var.set(caption)
        # update UI text
        self.status_var.set(os.path.basename(path))
        # draw
        self._update_image_on_canvas()
        # play sound on change (non-blocking)
        self._play_sound()
        # save last index to settings
        self.settings["last_index"] = real_index
        save_settings(self.settings)

    # ---------------- points & profile ----------------
    def _award_points(self, n=1):
        # small reward for viewing / interacting
        profile = self.profile
        profile["points"] = profile.get("points", 0) + n
        # level calc: every 100 points is a level
        profile["level"] = profile.get("points", 0) // 100 + 1
        self.settings["profile"] = profile
        save_settings(self.settings)
        self.profile = profile
        self.points_label.config(text=f"Points: {self.profile['points']}")
        self.level_label.config(text=f"Level: {self.profile['level']}")

    # ---------------- favorites ----------------
    def mark_favorite(self):
        if not hasattr(self, "_current_path") or not self._current_path:
            return
        try:
            src = self._current_path
            dst_name = os.path.basename(src)
            dst = os.path.join(FAV_DIR, dst_name)
            # avoid overwrite
            base, ext = os.path.splitext(dst)
            i = 1
            while os.path.exists(dst):
                dst = f"{base}_{i}{ext}"
                i += 1
            shutil.copy2(src, dst)
            self.status_var.set(f"Saved to favorites: {os.path.basename(dst)}")
            self._award_points(10)  # extra points for favoriting
        except Exception as e:
            self.status_var.set(f"Favorite failed: {e}")

    def export_favorites_zip(self):
        # zip the favorites folder
        if not os.path.exists(FAV_DIR):
            messagebox.showinfo("Export Favorites", "No favorites to export.")
            return
        zname = os.path.join(BASE_DIR, f"favorites_{time.strftime('%Y%m%d_%H%M')}.zip")
        try:
            with zipfile.ZipFile(zname, "w", zipfile.ZIP_DEFLATED) as zf:
                for fn in os.listdir(FAV_DIR):
                    path = os.path.join(FAV_DIR, fn)
                    zf.write(path, arcname=fn)
            messagebox.showinfo("Export Favorites", f"Exported to {zname}")
        except Exception as e:
            messagebox.showerror("Export Failed", str(e))

    # ---------------- import images ----------------
    def import_images(self):
        files = filedialog.askopenfilenames(title="Select images to add", filetypes=[("Images", "*.png;*.jpg;*.jpeg;*.gif;*.bmp;*.webp")])
        if not files:
            return
        copied = 0
        for f in files:
            try:
                dst = os.path.join(IMAGES_DIR, os.path.basename(f))
                # avoid overwrite
                base, ext = os.path.splitext(dst)
                i = 1
                while os.path.exists(dst):
                    dst = f"{base}_{i}{ext}"
                    i += 1
                shutil.copy2(f, dst)
                copied += 1
            except Exception as e:
                print("Import error:", e)
        if copied:
            # refresh images
            self.images = find_images(IMAGES_DIR)
            self.index_list = list(range(len(self.images)))
            if self.settings.get("shuffle"):
                random.shuffle(self.index_list)
            self._render_progress_dots()
            self.status_var.set(f"Imported {copied} images.")
            # show newly added image
            self.current_pos = 0
            self.show_image_at(self.current_pos, force=True)
            if self.is_playing:
                self.schedule_next()

    # ---------------- sound ----------------
    def _play_sound(self):
        if PYGAME_AVAILABLE and os.path.exists(SOUND_PATH):
            try:
                # restart sound in a background thread to avoid any blocking
                threading.Thread(target=lambda: pygame.mixer.music.play(), daemon=True).start()
            except Exception:
                pass

    # ---------------- fullscreen ----------------
    def toggle_fullscreen(self):
        is_full = bool(self.root.attributes("-fullscreen"))
        self.root.attributes("-fullscreen", not is_full)

    # ---------------- closing / persist ----------------
    def on_close(self):
        # save settings & profile
        self.settings["interval"] = int(self.interval_var.get())
        self.settings["shuffle"] = bool(self.settings.get("shuffle", False))
        self.settings["profile"] = self.profile
        save_settings(self.settings)
        self.cancel_timer()
        self.root.destroy()

# ----------------------------
# Run app
# ----------------------------
def main():
    ensure_dirs()
    root = tk.Tk()
    app = AffirmationApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
