import tkinter as tk
from tkinter import messagebox, simpledialog
import json, os
from datetime import datetime
from PIL import Image, ImageTk

WIDTH = 800
HEIGHT = 800

TASKS_FILE = "tasks.json"
SETTINGS_FILE = "settings.json"

# XP required per level
LEVEL_XP = 100


class SimpleTodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title(" To-Do By Arjeet🌸")
        self.root.geometry(f"{WIDTH}x{HEIGHT}")
        self.root.resizable(False, False)
        self.root.configure(bg="#ffdce9")

        # Load data
        self.tasks = self.load_json(TASKS_FILE, [])
        self.settings = self.load_json(SETTINGS_FILE, {
            "xp": 0,
            "level": 1,
            "points": 0
        })

        # Load minimal decorative icons
        self.images = {}
        self.load_icons()

        # UI
        self.build_header()
        self.build_input()
        self.build_task_list()
        self.build_footer()

        # Update screen
        self.refresh_tasks()
        self.draw_xp_bar()

    # ------------------------------
    # Data Utilities
    # ------------------------------
    def load_json(self, path, default):
        if os.path.exists(path):
            try:
                with open(path, "r") as f:
                    return json.load(f)
            except:
                pass
        return default

    def save_all(self):
        with open(TASKS_FILE, "w") as f:
            json.dump(self.tasks, f, indent=2)

        with open(SETTINGS_FILE, "w") as f:
            json.dump(self.settings, f, indent=2)

    # ------------------------------
    # Load Icons
    # ------------------------------
    def load_icons(self):
        try:
            t_img = Image.open("images/tulip.png").resize((50, 50))
            b_img = Image.open("images/butterfly.png").resize((50, 50))
            self.images["tulip"] = ImageTk.PhotoImage(t_img)
            self.images["butterfly"] = ImageTk.PhotoImage(b_img)
        except:
            self.images["tulip"] = None
            self.images["butterfly"] = None

    # ------------------------------
    # Header
    # ------------------------------
    def build_header(self):
        frame = tk.Frame(self.root, bg="#ffdce9")
        frame.pack(pady=10)

        if self.images["tulip"]:
            tk.Label(frame, image=self.images["tulip"], bg="#ffdce9").pack()

        tk.Label(
            frame,
            text="Simple To-Do App 🌸",
            font=("Comic Sans MS", 20, "bold"),
            fg="#c15ea8",
            bg="#ffdce9"
        ).pack()

        tk.Label(
            frame,
            text="Stay cute. Stay productive 🌸",
            font=("Comic Sans MS", 10),
            fg="#b24c93",
            bg="#ffdce9"
        ).pack()

    # ------------------------------
    # Input Section
    # ------------------------------
    def build_input(self):
        frame = tk.Frame(self.root, bg="#ffdce9")
        frame.pack(pady=10)

        self.entry = tk.Entry(
            frame,
            font=("Comic Sans MS", 14),
            width=20,
            bd=2,
            relief="flat",
            bg="white"
        )
        self.entry.grid(row=0, column=0, padx=5)

        tk.Button(
            frame,
            text="+",
            command=self.add_task,
            font=("Comic Sans MS", 16, "bold"),
            bg="#ffb7d9",
            fg="#7b2d63",
            bd=0,
            width=3
        ).grid(row=0, column=1)

    # ------------------------------
    # Task List Section
    # ------------------------------
    def build_task_list(self):
        frame = tk.Frame(self.root, bg="#ffdce9")
        frame.pack(fill="both", expand=True)

        self.task_frame = tk.Frame(frame, bg="#ffdce9")
        self.task_frame.pack(pady=10)

    def refresh_tasks(self):
        for widget in self.task_frame.winfo_children():
            widget.destroy()

        for task in self.tasks:
            self.draw_task(task)

    def draw_task(self, task):
        box = tk.Frame(self.task_frame, bg="white", bd=0)
        box.pack(fill="x", pady=6, padx=20)

        title = tk.Label(
            box,
            text=("✓ " if task["done"] else "✿ ") + task["title"],
            font=("Comic Sans MS", 14),
            bg="white",
            fg="#6b355e" if not task["done"] else "#b498ad"
        )
        title.pack(side="left", padx=10)

        # Check button
        tk.Button(
            box,
            text="✔",
            command=lambda t=task: self.toggle_complete(t),
            font=("Comic Sans MS", 10),
            bg="#ffd6eb",
            bd=0
        ).pack(side="right", padx=3)

        # Edit
        tk.Button(
            box,
            text="✎",
            command=lambda t=task: self.edit_task(t),
            font=("Comic Sans MS", 10),
            bg="#ffd6eb",
            bd=0
        ).pack(side="right", padx=3)

        # Delete
        tk.Button(
            box,
            text="🗑",
            command=lambda t=task: self.delete_task(t),
            font=("Comic Sans MS", 10),
            bg="#ffd6eb",
            bd=0
        ).pack(side="right", padx=3)

    # ------------------------------
    # Task Actions
    # ------------------------------
    def add_task(self):
        title = self.entry.get().strip()
        if not title:
            return
        task = {
            "id": int(datetime.now().timestamp()),
            "title": title,
            "done": False,
            "created": datetime.now().isoformat()
        }
        self.tasks.insert(0, task)
        self.entry.delete(0, tk.END)
        self.save_all()
        self.refresh_tasks()

    def edit_task(self, task):
        new = simpledialog.askstring("Edit", "Edit task:", initialvalue=task["title"])
        if new:
            task["title"] = new.strip()
            self.save_all()
            self.refresh_tasks()

    def delete_task(self, task):
        self.tasks = [t for t in self.tasks if t["id"] != task["id"]]
        self.save_all()
        self.refresh_tasks()

    def toggle_complete(self, task):
        task["done"] = not task["done"]

        if task["done"]:
            self.give_xp(5)
            self.spawn_heart()

        self.save_all()
        self.refresh_tasks()

    def clear_completed(self):
        self.tasks = [t for t in self.tasks if not t["done"]]
        self.save_all()
        self.refresh_tasks()

    # ------------------------------
    # XP System
    # ------------------------------
    def give_xp(self, amount):
        self.settings["xp"] += amount
        self.settings["points"] += amount

        if self.settings["xp"] >= LEVEL_XP:
            self.settings["xp"] = 0
            self.settings["level"] += 1
            messagebox.showinfo("Level Up!", "You reached a new level! 🌟")

        self.save_all()
        self.draw_xp_bar()

    # ------------------------------
    # Footer XP Bar
    # ------------------------------
    def build_footer(self):
        frame = tk.Frame(self.root, bg="#ffdce9")
        frame.pack(pady=10)

        tk.Label(
            frame,
            text="Progress 💖",
            font=("Comic Sans MS", 12),
            bg="#ffdce9",
            fg="#b24c93"
        ).pack()

        self.xp_canvas = tk.Canvas(frame, width=300, height=20, bg="#ffc8df", bd=0, highlightthickness=0)
        self.xp_canvas.pack()

        self.points_label = tk.Label(
            frame,
            text=f"Points: {self.settings['points']}",
            font=("Comic Sans MS", 10),
            bg="#ffdce9",
            fg="#9b2e78"
        )
        self.points_label.pack()

        self.level_label = tk.Label(
            frame,
            text=f"Level: {self.settings['level']}",
            font=("Comic Sans MS", 10),
            bg="#ffdce9",
            fg="#9b2e78"
        )
        self.level_label.pack()

    def draw_xp_bar(self):
        self.xp_canvas.delete("all")
        xp = self.settings["xp"]
        fill_w = int((xp / LEVEL_XP) * 300)
        self.xp_canvas.create_rectangle(0, 0, fill_w, 20, fill="#ff8ac4", width=0)

        self.points_label.config(text=f"Points: {self.settings['points']}")
        self.level_label.config(text=f"Level: {self.settings['level']}")

    # ------------------------------
    # Heart Animation (simple)
    # ------------------------------
    def spawn_heart(self):
        heart = tk.Label(self.root, text="💗", font=("Comic Sans MS", 20), bg="#ffdce9")
        heart.place(x=200, y=500)

        def animate(step=0):
            if step > 20:
                heart.destroy()
                return
            heart.place(x=200, y=500 - step * 5)
            heart.after(30, lambda: animate(step+1))

        animate()


# ------------------------------
# Run app
# ------------------------------
if __name__ == "__main__":
    root = tk.Tk()
    app = SimpleTodoApp(root)
    root.mainloop()
