🍅 Pomodoro Timer App

A clean, modern Pomodoro Timer designed to help you stay productive, focused, and consistent.
Built as Day 3 of the 30 Days 30 Projects challenge.

✨ Features
🎨 Design

Minimal UI: Clean, distraction-free layout

Large Timer Display: Easy-to-read session countdown

Smooth Animations: Subtle transitions for timer and buttons

Responsive Layout: Works on desktop & mobile

Ambient Mode: Optional rain sound for deep focus

⏱ Productivity Functionality

Work Timer: Default 25 minutes (fully customizable)

Short Break: Default 5 minutes

Long Break: After every 4 cycles

Auto-Switch: Automatically shifts between work → break → work

Session Counter: Tracks how many pomodoros completed today

Motivational Status Messages: Encouraging text for each session

🔊 Audio System

Session Notification: Alert sound when a session ends

Ambient Rain Sound: Looping background rain (light_rain.wav)

Toggle Control: Turn ambient sound on/off anytime

Smart Audio: Automatically pauses during reset

⌨️ Keyboard Support

Space: Start/Pause the timer

R: Reset session

S: Skip current session

L: Log a completed pomodoro manually

🚀 Getting Started
Prerequisites

Modern web browser (Chrome, Firefox, Safari, Edge)

Installation

Clone the repository:

git clone https://github.com/Arjeetkumar/30-day-projects.git
cd day3

Run Web Version

Just open:

index.html


No server required.

📂 Project Structure
day3/
├── index.html          # Main HTML structure
├── style.css           # Styling and animations
├── script.js           # Pomodoro logic and event handlers
├── light_rain.wav      # Ambient audio file
└── README.md           # Documentation

🎯 How to Use
Web Pomodoro Timer

Start Session: Click Start

Pause Anytime: Click Pause or press Space

Reset Session: Click Reset or press R

Skip Session: Skip to next cycle

Ambient Mode: Toggle rain sound for focus

Settings: Customize work & break durations

What Happens Automatically

After work session → starts break

After break → starts new work session

After 4 cycles → long break starts

Daily pomodoro count saved locally

💻 Code Highlights
Auto Switching Logic
if (mode === "work") {
    mode = "break";
} else if (cycleCount % 4 === 0) {
    mode = "long-break";
}
startTimer();

Rain Sound Toggle
rainBtn.addEventListener("click", () => {
    if (rainAudio.paused) {
        rainAudio.play();
    } else {
        rainAudio.pause();
    }
});

Session Completion Alert
alertSound.play();
setTimeout(() => {
    alert("Session Complete!");
}, 300);

🎨 Styling Details
Color Palette

Primary Red: #ff5a5f

Background Dark: #0d1b2a

Mint Blue: #4dd0e1

Warning Yellow: #ffa726

Soft Gray: #90a4ae

Typography

System fonts (Segoe UI, Roboto, Inter)

Responsive Design
@media (max-width: 480px) {
    .timer {
        font-size: 58px;
    }
    .controls button {
        width: 140px;
        height: 50px;
    }
}

🛠️ Technologies Used

HTML5: Semantic layout

CSS3: Flexbox, Grid, animations

JavaScript: Timer logic, event handling, audio system

Audio: WAV/MP3 for session + rain sound

🔮 Future Enhancements

 Task list integration

 Dark/Light theme switch

 Daily statistics dashboard

 Weekly productivity graph

 Custom notification tones

 Full-screen focus mode

🐛 Known Issues

Ambient audio may autoplay-blocked on some browsers

Rapid start/pause may cause minor timer drift

1-second delay in certain browsers due to JS setInterval timing

📝 Learning Outcomes

This project helped practice:

Timer development using JavaScript

Audio controls & HTML5 Audio API

UI design and responsive layout

Custom event handling

Managing focus-oriented workflows

Building practical productivity tools

👨‍💻 Author

Arjeet Kumar
GitHub: @Arjeetkumar

Project: 30 Days 30 Projects

📄 License

This project is part of the 30 Days 30 Projects challenge and is open-source.

🙏 Acknowledgments

Inspired by classic Pomodoro productivity techniques

Part of the 30 Days 30 Projects challenge

Ambient rain generated using custom audio script

Day 3 of 30 | Built with ❤️ and ☕