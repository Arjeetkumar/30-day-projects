💧 Hydration Timer App

A beautifully designed hydration reminder app with a clean UI, smooth visuals, audio alerts, progress tracking, and fully customizable timer settings.
Built as Day 2 of the 30 Days 30 Projects challenge.

🖼️ Hydration Timer Preview

(Add your app screenshot here)
Example:
<img src="images/fancy_full3.png" width="400">

✨ Features
🎨 Design

Clean Dark-Themed UI: Modern layout with glass-like elements

Water-Level Animations: 7-stage water glass levels

Responsive Interface: Scales smoothly across screens

Highlighted Buttons & Cards: Rounded, elegant visuals

⏱️ Timer & Functionality

Fully Custom Timer: Set your drinking interval in minutes

Daily Water Goal: Choose how many glasses you aim to drink per day

Persistent Tracking: Saves count & goal automatically

Progress Bar: See daily progress visually

Manual Logging: Add glasses manually when needed

Timer Auto-Reset: After every cycle

🔔 Alarm System

Looping Alarm: Plays until user clicks OK

MP3 & WAV Support: Uses any alarm file you provide

pygame Integration: Clear looping audio

Graceful Fallback: App functions even without sound

⌨️ Keyboard Support

Space → Start/Pause

Escape → Reset

D → Log a glass instantly

🚀 Getting Started
Prerequisites

Python 3.x installed

Pillow → pip install pillow

Optional (for alarm): pygame → pip install pygame

Installation

Clone the repository:

git clone https://github.com/YourUsername/30Days-30Projects.git
cd day2


Run the app:

python timer.py

📂 Project Structure
day2/
├── timer.py              # Main Hydration Timer App
├── hydration.json        # Auto-generated saved state
├── alarm.mp3             # Alarm audio (optional)
├── alarm.wav             # Alternative alarm file
├── README.md             # Documentation
└── images/
    ├── full.png
    ├── full1.png
    ├── full2.png
    ├── full3.png
    ├── full4.png
    ├── full5.png
    └── full6.png


If no images are present, the app generates placeholders automatically.

🎯 How to Use
Hydration Timer

Set your timer duration (in minutes)

Click Apply

Press START

When the timer ends:

Alarm will loop

Popup reminds you to drink

Click OK → timer resets

Daily Goal Tracking

Set your daily water intake goal

App saves it to hydration.json

Progress bar updates instantly

Manual Logging

Click I DRANK (LOG)

Or press D to instantly add

💻 Code Highlights
Dynamic Timer Setting
mins = int(self.minutes_var.get())
self.total_time = mins * 60
self.remaining_time = self.total_time

Daily Progress Visualization
percent = int((self.water_count / max(1, self.daily_goal)) * 100)
self.progress['value'] = min(100, percent)

Auto-Saving State
with open("hydration.json", "w") as f:
    json.dump({"count": self.water_count, "goal": self.daily_goal}, f)

Continuous Alarm Loop
pygame.mixer.music.load(self.alarm_path)
pygame.mixer.music.play(-1)

🎨 Styling Details

Color Palette

Navy Background: #0d1b2a

Aqua Accent: #4dd0e1

Light Gray: #90a4ae

Deep Card Blue: #1a2f45

Warning Orange: #ffa726

Purple Log Button: #7c4dff

Visuals

Water glass animation

Gradient progress UI

Rounded buttons

Crisp typography

🛠️ Technologies Used

Python Tkinter — GUI

Pillow (PIL) — images

pygame — audio

JSON — storing user data

🔮 Future Enhancements

Daily reset at midnight

Sound volume slider

Snooze reminder feature

Water intake history chart

Multiple sound themes

Mobile/desktop packaged version

🐛 Known Issues

Alarm needs pygame for best experience

Without images, placeholders appear

Some OSes handle audio differently

📚 Learning Outcomes

This project helped practice:

Event-driven Tkinter programming

Image loading & UI state management

Timer events with after()

Data persistence using JSON

Playing audio reliably

Designing a health-reminder tool

Creating user-friendly UI layouts

👨‍💻 Author

Arjeet Kumar
GitHub: Add your GitHub link here
Project: 30 Days 30 Projects

📄 License

This project is a part of the 30 Days 30 Projects challenge and is fully open source.

🙏 Acknowledgments

Inspired by popular hydration reminder apps

Visual enhancements customized for this challenge

Sound, UI layout & design refined for simplicity and clarity

Day 2 of 30 | Built with 💧 discipline and ⚡ consistency by Arjeet Kumar