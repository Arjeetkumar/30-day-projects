## 💧Day2- Hydration Timer App

A beautifully designed hydration reminder app with a clean UI, smooth visuals, audio alerts, progress tracking, and fully customizable timer settings.
Built as Day 2 of the 30 Days 30 Projects challenge.

## 🖼️ Hydration Timer Preview

<img width="1033" height="1003" alt="Screenshot 2025-11-19 130044" src="https://github.com/user-attachments/assets/fad0511c-c3df-4ad8-a663-12710b1076b1" />

### ✨ Features
## 🎨 Design

- Clean Dark-Themed UI: Modern layout with glass-like elements

- Water-Level Animations: 7-stage water glass levels

- Responsive Interface: Scales smoothly across screens

- Highlighted Buttons & Cards: Rounded, elegant visuals

## ⏱️ Timer & Functionality

- Fully Custom Timer: Set your drinking interval in minutes

- Daily Water Goal: Choose how many glasses you aim to drink per day

- Persistent Tracking: Saves count & goal automatically

- Progress Bar: See daily progress visually

- Manual Logging: Add glasses manually when needed

- Timer Auto-Reset: After every cycle

## 🔔 Alarm System

- Looping Alarm: Plays until user clicks OK

- MP3 & WAV Support: Uses any alarm file you provide

- pygame Integration: Clear looping audio

- Graceful Fallback: App functions even without sound

- ⌨️ Keyboard Support

- Space → Start/Pause

- Escape → Reset

- D → Log a glass instantly


## Clone the repository:

git clone https://github.com/Arjeetkumar/30Days-30Projects.git

## 📂 Project Structure
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
    └── full6.png.

## 🎯 How to Use
- Hydration Timer

- Set your timer duration (in minutes)

- Click Apply

- Press START

- When the timer ends:

- Alarm will loop

- Popup reminds you to drink

- Click OK → timer resets

- Daily Goal Tracking

- Set your daily water intake goal

- App saves it to hydration.json

- Progress bar updates instantly

- Manual Logging

- Click I DRANK (LOG)

- Or press D to instantly add

## 🎨 Styling Details

### Color Palette

- Navy Background: #0d1b2a

- Aqua Accent: #4dd0e1

- Light Gray: #90a4ae

- Deep Card Blue: #1a2f45

- Warning Orange: #ffa726

- Purple Log Button: #7c4dff

## 🛠️ Technologies Used

- Python Tkinter — GUI

- Pillow (PIL) — images

- pygame — audio

- JSON — storing user data

## 🔮 Future Enhancements

- Daily reset at midnight

- Sound volume slider

- Snooze reminder feature

- Water intake history chart

- Multiple sound themes

- Mobile/desktop packaged version

## 🐛 Known Issues

- Alarm needs pygame for best experience

- Without images, placeholders appear

- Some OSes handle audio differently

## 📚 Learning Outcomes

### This project helped practice:

- Event-driven Tkinter programming

- Image loading & UI state management

- Timer events with after()

- Data persistence using JSON

- Playing audio reliably

- Designing a health-reminder tool

- Creating user-friendly UI layouts

## 👨‍💻 Author

## Arjeet Kumar
GitHub: https://github.com/Arjeetkumar/30-day-projects/edit/main/day2

Day 2 of 30 | Built with 💧 discipline and ⚡ consistency by Arjeet Kumar
Project: 30 Days 30 Projects

