# 🧮 Day 1 — Neo Glassmorphism Calculator

A futuristic, glass-effect calculator with glowing buttons, smooth animations, advanced keyboard support, and clean JavaScript logic.
Built as Day 1 of the 30 Days 30 Projects Challenge.

### ✨ Features
## 🎨 Modern UI (Unique Design)

- Glassmorphism style with blur effects

- Soft neon-glow buttons

- Gradient background

- Floating rounded keys

- Animated header

## 🔢 Calculator Functionality

- Addition, subtraction, multiplication, division

- Decimal point support

- Negative number toggle (+/-)

- Backspace/delete

- Prevents invalid decimal inputs

- Prevents division by zero

- Smooth, continuous calculations

## ⌨️ Keyboard Support

- Numbers (0–9)

- Operators (+, –, *, /)

- Enter → Equals

- Backspace → Delete last digit

- Escape → Clear all

- “.” → Decimal

- “n” → Toggle negative number

## 📱 Responsive

- Dynamic layout for mobile screens

- Auto-resizing display text

- Touch-friendly buttons

## 📸 UI Preview

<img width="622" height="832" alt="Screenshot 2025-11-18 124804" src="https://github.com/user-attachments/assets/6533158c-433e-4d5f-b02d-7bfc455437f4" />

## 🛠️ Tech Stack

- HTML5 – Markup

- CSS3 – Glassmorphism + Grid/Flexbox

- JavaScript (Vanilla) – Calculator logic + keyboard events

## 📂 Project Structure
day1/
├── index.html          # UI Structure
├── style.css           # Glassmorphism Styling
├── script.js           # Calculator Logic
└── README.md           # Documentation

### 🚀 Getting Started
## 📦 Clone the Repository
git clone https://github.com/Arjeetkumar/30-day-projects.git
cd day1

## ▶️ Run the Web Version
http://127.0.0.1:5500/day1/

## 🔮 Future Enhancements

- History panel

- Dark/Light themes

- Scientific mode

- Sound effects

- Button animations on press

- LocalStorage memory

## 📚 Learning Outcomes

# This project helped practice:

- Event-driven JavaScript

- State management

- UI/UX design

- Keyboard event handling

- Grid-based layouting

- Glassmorphism design

- Clean function-based logic

## 👨‍💻 Author
# Arjeet kumar
30 Days 30 Projects Challenge

Day 1 of 30 | Built with 💖 and ☕Arjeet Kumar


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

# 🍅 Day3 - Pomodoro Timer App

A clean, modern Pomodoro Timer designed to help you stay productive, focused, and consistent.
Built as Day 3 of the 30 Days 30 Projects challenge.

## Pomodoro Timer Preview
<img width="1203" height="831" alt="Screenshot 2025-11-20 094519" src="https://github.com/user-attachments/assets/4539639b-64ce-4198-ae42-6754d00838c1" />

### ✨ Features
## 🎨 Design

- Minimal UI: Clean, distraction-free layout

- Large Timer Display: Easy-to-read session countdown

- Smooth Animations: Subtle transitions for timer and buttons

- Responsive Layout: Works on desktop & mobile

- Ambient Mode: Optional rain sound for deep focus

## ⏱ Productivity Functionality

- Work Timer: Default 25 minutes (fully customizable)

- Short Break: Default 5 minutes

- Long Break: After every 4 cycles

- Auto-Switch: Automatically shifts between work → break → work

- Session Counter: Tracks how many pomodoros completed today

- Motivational Status Messages: Encouraging text for each session

## 🔊 Audio System

- Session Notification: Alert sound when a session ends

- Ambient Rain Sound: Looping background rain (light_rain.wav)

- Toggle Control: Turn ambient sound on/off anytime

- Smart Audio: Automatically pauses during reset

## ⌨️ Keyboard Support

- Space: Start/Pause the timer

- R: Reset session

- S: Skip current session

- L: Log a completed pomodoro manually

### Clone the repository:

git clone https://github.com/Arjeetkumar/30-day-projects.git

## 📂 Project Structure
day3/
├── index.html          # Main HTML structure
├── style.css           # Styling and animations
├── script.js           # Pomodoro logic and event handlers
├── light_rain.wav      # Ambient audio file
└── README.md           # Documentation

## 🎯 How to Use
- Web Pomodoro Timer

- Start Session: Click Start

- Pause Anytime: Click Pause or press Space

- Reset Session: Click Reset or press R

- Skip Session: Skip to next cycle

- Ambient Mode: Toggle rain sound for focus

- Settings: Customize work & break durations

- What Happens Automatically

- After work session → starts break

- After break → starts new work session

- After 4 cycles → long break starts

- Daily pomodoro count saved locally

## 🛠️ Technologies Used

- HTML5: Semantic layout

- CSS3: Flexbox, Grid, animations

- JavaScript: Timer logic, event handling, audio system

- Audio: WAV/MP3 for session + rain sound

## 🔮 Future Enhancements

- Task list integration

 - Dark/Light theme switch

 - Daily statistics dashboard

 - Weekly productivity graph

 - Custom notification tones

 - Full-screen focus mode

## 🐛 Known Issues

- Ambient audio may autoplay-blocked on some browsers

- Rapid start/pause may cause minor timer drift

- 1-second delay in certain browsers due to JS setInterval timing

## 📝 Learning Outcomes

- Timer development using JavaScript

- Audio controls & HTML5 Audio API

- UI design and responsive layout

- Custom event handling

- Managing focus-oriented workflows

- Building practical productivity tools

## 👨‍💻 Author

### Arjeet Kumar
GitHub: @Arjeetkumar

Project: 30 Days 30 Projects

# 🌟Day 4 - Daily Affirmation Viewer

A beautifully designed desktop affirmation viewer that displays uplifting images, motivational text, and plays soft sound effects — all while tracking your progress with a gamified points system.

## Affirmation View
<img width="1114" height="778" alt="Screenshot 2025-11-20 193251" src="https://github.com/user-attachments/assets/c92a8433-eb98-412f-922f-3e7f835ebf5f" />

### ✨ Features
## 🎨 Design & UI

- Clean, minimal dark-themed UI

- Smooth auto-scaling of images

- Centered canvas display with dynamic resizing

- Soft caption overlay with motivational quotes

- Progress indicator dots (up to 20 images)

- Beautiful button layout with modern styling

## 🖼️ Image Features

- Auto-loads all images from /images/ folder

- Supports: PNG, JPG, JPEG, GIF, BMP, WEBP

- Auto-resizes images to fit the window

- Smart detection of missing/broken images

- Shuffle mode for random inspiration

- Favorite any image (saved to /favorites/)

- Export your favorites as a ZIP file

## ⏱️ Slideshow Features

- Auto-slide every X seconds (default: 3s)

- Adjustable interval via UI

## Keyboard shortcuts:

- ⏩ Right Arrow → Next image

- ⏪ Left Arrow → Previous image

- ⏯ Space → Play / Pause

- 🔀 S → Shuffle on/off

- 📺 F → Fullscreen toggle

- ➕ / ➖ → Increase/decrease interval

- 📥 N → Add new images

  ## 🔊 Sound System

- Plays sound.mp3 on each slide transition

- Runs sound in a non-blocking background thread

- Works automatically if pygame is installed



## 🎮 Gamification — Points & Levels

A fun way to stay motivated!

You earn:

- +1 point for viewing each new affirmation

- +10 points for marking favorites

- Automatic level-up every 100 points

###  Displayed in the UI:

- ⭐ Points

- 🥇 Level

## 📂 Folder Structure
day4/
├── affirmation_viewer.py    # Main application
├── images/                  # Add your affirmation images here
├── favorites/               # Saved favorite images
├── captions.txt             # Captions for images
├── settings.json            # Auto-generated user settings
└── sound.mp3                # Slide transition sound

## 🐛 Known Issues

- Very long captions may overflow on extremely small windows

- GIF animations currently show first frame (Tkinter limitation)

- Sound requires pygame installed — otherwise skipped silently

## 🔮 Future Enhancements

- Add background music mode

- Add "Daily Streak" tracker

- Add category folders inside /images

- Add transitions: fade, slide-in

- Add image filters (warmth, glow, brightness)

- Add drag-and-drop image import

## 🧠 Learning Outcomes

This project helped practice:

- Tkinter canvas & UI layout

- Image processing with Pillow (PIL)

- Non-blocking sound threads

- File system operations & persistence

- Gamification logic (points & leveling)

- Designing clean, modern desktop apps

## 👨‍💻 Author

### Arjeet Kumar
30 Days 30 Projects Challenge

# 🌸 Day 5 - Simple To-Do App

A pastel-themed, gamified To-Do application with cute animations, XP system, and a mobile-style UI — built as Day 5 of the 30 Days 30 Projects challenge by Arjeet.

✨ Preview
<img width="986" height="1011" alt="Screenshot 2025-11-22 150222" src="https://github.com/user-attachments/assets/37d2f2d8-fedf-44fb-8dfd-ca38ea552ad8" />

A beautifully designed productivity app featuring a pink kawaii interface, butterflies, tulips, animations, and smooth task management.

### 🎀 Features
## 🎨 Design

- Kawaii Pastel UI: Soft pink background and bubble-style elements

- Cute Icons: Tulip 🌷 & Butterfly 🦋 decorations

- Mobile Layout: 450×800 design for a compact look

- Simple & Clean Interface: Easy to use

- Comic Sans Bubble Font: Soft, rounded, aesthetic

## 📝 Task Management

- Add tasks

- Edit tasks

- Delete tasks

- Mark tasks as complete

- Clear completed tasks

- Auto-save to JSON

- Smooth task re-rendering

## ⭐ Gamified Progress System

- Earn XP for completing tasks

- Earn points (same as XP)

- Level up every 100 XP

- Visual XP progress bar

- Level popup effect

## 💗 Cute Animations

- Floating heart pop animation whenever a task is completed

## 💾 Auto Saving

Your data is stored locally:

- tasks.json
- settings.json

## 📁 Project Structure
day5/
│── to_do.py              # Main application
│── tasks.json            # Saved tasks
│── settings.json         # XP + Level + Points
└── images/
     ├── tulip.png        # Header icon
     └── butterfly.png    # Decoration icon
     
## 🎨 UI Elements

- 🌷 Tulip Icon	Header decoration
- 🦋 Butterfly Icon	Decorative element
- 💗 Heart Pop	Floating animation on completion
- ⭐ XP Bar	Shows your progress toward next level
- 🎀 Pink Palette	Soft kawaii aesthetic
- 📱 Mobile Layout	450×800 window
  
## 🛠 Technologies Used

- Python 3

- Tkinter (GUI)

- Pillow (Image processing)

- JSON (Local Storage)

## 🔮 Future Enhancements

- Add themes (Purple / Blue / Dark Mode)

- Add categories (Work / Study / Personal)

- Add search bar

- Add task reminders

- Add cloud sync

- Add streak system

- Add daily motivational quotes

- Add custom icons

## 🐛 Known Issues

- Old tasks.json may cause errors if it uses old keys

- Large numbers of tasks may extend the scroll area (update planned)

## 📝 Learning Outcomes

This project helped practice:

- Tkinter GUI development

- Working with JSON storage

- Event handling

- Basic animations

- Clean UI layout design

- XP/Progress systems

- Image loading with Pillow

- Mobile-style GUI architecture

## 👨‍💻 Author

### Arjeet
Passionate about Python 
GitHub: @Arjeetkumar

Project: 30 Days 30 Projects

# 🎵  Day 6 - Neon Lyrics Visualizer

A futuristic, cyberpunk-inspired music visualizer with synced lyrics (LRC), glowing audio bars, neon animations, and a fully responsive hologram-style UI.
Built as Day 6 of the 30 Days, 30 Projects challenge.

## 🎬 Preview (UI Overview)
<img width="1916" height="891" alt="Screenshot 2025-11-23 171111" src="https://github.com/user-attachments/assets/8acb0010-9658-404e-9b66-4c1bd6598d88" />

## A modern neon interface featuring:

- Holographic lyric panel

- Bass-reactive glow

- Mirror waveform bars

- Cyberpunk glass sidebar

- Smooth animations

- Real-time lyric syncing

### ✨ Features
## 🎨 Design

- Cyberpunk HUD UI

- Glassmorphism Sidebar

- Neon Glow Effects (Cyan + Purple + Pink)

- Responsive Layout

- Animated Waveform Canvas

- Futuristic Fonts (Orbitron, Rajdhani)

- Smooth transitions on text + panels

## 🎵 Audio Features

- Upload any MP3 file instantly

- AudioContext (Web Audio API) powered analyzer

- Real-time frequency bars

- Dual-wave mirror effect (Top + Bottom bars)

- Beat detection → auto text scaling

## 📝 Lyrics Features

- Supports LRC Timestamped Lyrics like Spotify / YouTube Music

### Example format:

[00:12.50] Line 1 here
[00:15.80] Another synced line

## ✍️ Text Controls

- Adjustable text size

- Adjustable glow intensity

- Dynamic neon pulse based on bass

## 🕹️ Controls

- Play / Pause buttons

- Load MP3

- Load Lyrics

- Demo Mode

- Fully keyboard-safe and responsive



  ### git clone https://github.com/Arjeetkumar/30-day-projects/edit/main/day6

## 📂 Project Structure
NeonVisualizer/
│
├── index.html        # Main HTML structure
├── style.css         # UI styling (neon + glassmorphism)
├── script.js         # Visualizer logic + LRC syncing
├── assets/           # (Optional) Backgrounds, icons, UI extras
└── README.md         # Documentation (this file)

## 🎨 Styling Details
Color Palette

- Cyan (Primary): #00f3ff

- Purple (Secondary): #bc13fe

- Neon Pink (Accent): #ff0055

- Dark Background: #050510

Glow Shadows

- Text & bars have layered glow:

- text-shadow: 
   0 0 20px var(--primary),
   0 0 40px var(--secondary);

- Glass Sidebar
backdrop-filter: blur(20px);
background: rgba(255,255,255,0.05);

## 🔮 Future Enhancements

- Karaoke word-by-word highlight

- Auto lyric sync (AI beats detection)

- Multiple visualization modes

- Circular hologram waveform

- Background particle effects

- Import external LRC files

- Dark/Light neon color themes

## 🐛 Known Issues

- Some mobile browsers restrict AudioContext

- Large MP3 files may cause slight visual lag

- Missing LRC timestamps → fallback uses auto timing

## 📝 Learning Outcomes

This project teaches:

- Web Audio API

- Canvas API

- LRC format parsing

- State management

- DOM animation

- Cyberpunk UI design

- Glow / neon / glassmorphism effects

- Modular JS logic

- Event-driven programming in JS

## 👨‍💻 Author

### Made by Arjeet

From the 30 Days — 30 Projects Challenge

# 🎨 Day 7 - FaceArt AI

A modern AI-powered face transformation tool with stunning visuals, seamless UI, and smart SDXL image-to-image generation. Built as Day 7 of the 30 Days 30 Projects Challenge.

FaceArt AI allows users to upload any portrait photo and transform it into Pixar, Cyberpunk, Anime, Sketch, Claymation, Zombie, or any custom art style using Stable Diffusion XL.

### ✨ Features
## 🎨 Design

- Modern, glass-blur sidebar UI

- Neon accent colors with premium aesthetics

- Fully responsive and smooth animations

- Clean preview area with compare mode

- Loading overlay with “AI Dreaming” effect

## 🤖 AI Power

- Image-to-Image transformation using SDXL (Stable Diffusion XL)

- Smart auto-resizing to valid SDXL dimensions

- Adjustable creativity slider (10%–90%)

- Built-in style filters:

- Pixar

- Cyberpunk

- Anime

- Sketch

- Zombie

- Claymation

- Optional custom prompt for full creativity

- Instant result preview

- Hold-to-compare button to quickly toggle original vs AI image

## 📸 Upload & Output
<img width="1902" height="919" alt="Screenshot 2025-11-24 172353" src="https://github.com/user-attachments/assets/c19d6004-5e25-4115-a9ca-7e1c1c8c9e00" />

- Upload any JPG/PNG photo

- Automatically displayed in preview

- AI output generated in PNG

- One-click Download Result button

## git clone https://github.com/Arjeetkumar/30-day-projects/edit/main/day7

## 📂 Project Structure
FaceArt-AI/
├── index.html          # Main UI structure
├── style.css           # Neon UI, glass sidebar, transitions
├── script.js           # AI logic, API call, auto resizing, UI handling
├── assets/             # Optional: icons, backgrounds
└── README.md           # Documentation

## 🎨 Styling Details
### Color Palette
- Accent	#ff0055 (Neon Pink)
- Accent Gradient	Pink → Gold
- Background	#0f0c29 dark gradient
- Sidebar	Semi-transparent glass blur
- UI Components:

- Glassy neon buttons

- Dynamic shadows and glow

- Smooth hover effects

- Blurred glass sidebar

## 🔮 Future Enhancements

- Background remover + custom scene

- Change-gender, old-age, child-face filters

- Live camera mode

- HD upscale option

- Color-grading presets

- Face anonymization AI

- AI animations / video output (future)

## 🐛 Known Issues

- Very large images take longer to resize

- Some styles may alter facial identity too much at high strength

- API key must be manually added in script.js (insecure for production)

## 📝 Learning Outcomes

This project helped practice:

- Working with AI Image APIs (Stability AI)

- Image resizing + canvas manipulation

- Advanced UI/UX design with glassmorphism

- Handling Blobs, base64 conversion, and async file operations

- Creating dynamic sliders, filters, prompt builders

- Deep understanding of Image-to-Image AI workflows

- Building a complete web-app with no backend

## 👨‍💻 Author

### Arjeet Kumar
IIT Patna – BSc CS & Data Analysis

Day 7 – 30 Days 30 Projects Challenge
























