🌸 Kawaii To-Do App

A pastel-themed, gamified To-Do application with cute animations, XP system, and a mobile-style UI — built as Day 5 of the 30 Days 30 Projects challenge by Arjeet.

✨ Preview

A beautifully designed productivity app featuring a pink kawaii interface, butterflies, tulips, animations, and smooth task management.

🎀 Features
🎨 Design

Kawaii Pastel UI: Soft pink background and bubble-style elements

Cute Icons: Tulip 🌷 & Butterfly 🦋 decorations

Mobile Layout: 450×800 design for a compact look

Simple & Clean Interface: Easy to use

Comic Sans Bubble Font: Soft, rounded, aesthetic

📝 Task Management

Add tasks

Edit tasks

Delete tasks

Mark tasks as complete

Clear completed tasks

Auto-save to JSON

Smooth task re-rendering

⭐ Gamified Progress System

Earn XP for completing tasks

Earn points (same as XP)

Level up every 100 XP

Visual XP progress bar

Level popup effect

💗 Cute Animations

Floating heart pop animation whenever a task is completed

💾 Auto Saving

Your data is stored locally:

tasks.json
settings.json


No data is lost when app is closed.

📁 Project Structure
day5/
│── to_do.py              # Main application
│── tasks.json            # Saved tasks
│── settings.json         # XP + Level + Points
└── images/
     ├── tulip.png        # Header icon
     └── butterfly.png    # Decoration icon

🚀 Getting Started
✔ Prerequisites

Install Pillow:

pip install pillow

✔ Run the App

Navigate to your project folder:

cd day5
python to_do.py


The app will open in a pink mobile-style window.

🎮 How to Use
➕ Add a Task

Type in the entry box

Click + button

✏️ Edit a Task

Click ✎ icon

✔ Complete a Task

Click ✔ icon

You earn XP + Points

A cute 💗 heart pops!

🗑 Delete a Task

Click 🗑 icon

🧹 Clear Completed

Automatically handled when needed.

🎨 UI Elements
Element	Description
🌷 Tulip Icon	Header decoration
🦋 Butterfly Icon	Decorative element
💗 Heart Pop	Floating animation on completion
⭐ XP Bar	Shows your progress toward next level
🎀 Pink Palette	Soft kawaii aesthetic
📱 Mobile Layout	450×800 window
🛠 Technologies Used

Python 3

Tkinter (GUI)

Pillow (Image processing)

JSON (Local Storage)

🔮 Future Enhancements

Add themes (Purple / Blue / Dark Mode)

Add categories (Work / Study / Personal)

Add search bar

Add task reminders

Add cloud sync

Add streak system

Add daily motivational quotes

Add custom icons

🐛 Known Issues

Old tasks.json may cause errors if it uses old keys

Large numbers of tasks may extend the scroll area (update planned)

📝 Learning Outcomes

This project helped practice:

Tkinter GUI development

Working with JSON storage

Event handling

Basic animations

Clean UI layout design

XP/Progress systems

Image loading with Pillow

Mobile-style GUI architecture

👨‍💻 Author

Arjeet
Passionate about Python, UI design & building creative apps.
Day 5 of the 30 Projects in 30 Days Challenge ✨