⚡ Habit Quest — Cyberpunk Habit Tracker

A gamified, neon-themed habit tracker with XP, levels, streaks, animated progress rings, sound effects, import/export and beautiful glassmorphism UI. Built as Day 11 of the 30 Days 30 Projects challenge.

Project Preview

✨ Features
🎨 Design
Cyberpunk Neon UI: Glassmorphism, glowing gradients, animated blobs and neon accents.
Animated Progress Rings: SVG rings that animate on progress.
Responsive Layout: Cards grid that adapts from desktop to mobile.
Micro-interactions: Floating XP text, hover states, and level-up animations.

🔢 Functionality
Gamified Points System: Points per action + completion bonus for daily goals.
XP & Levels: Level up (every 500 XP by default) with celebration & sound.
Streak Tracking: Consecutive-day streak detection.
Create / Edit / Delete Habits: Custom name, daily goal, color, points, bonus.
Undo Actions: Revert the last increment for a habit.
Search Habits: Instant search to find habits quickly.
Export / Import: Save or restore app data (.json) for backup or migration.
Weekly Chart: View last 7 days of earned XP with tooltips.

🔊 Sound & Feedback
Web Audio API: Tick sound for actions, multi-tone for completion, melody for level-up.
Floating Notifications: +XP and LEVEL UP visual feedback.

💾 Persistence
localStorage: Data saved locally (habits, profile, history).
Safe Import/Export: JSON import with validation.

📱 UI Elements
Top bar with total points, level & progress bar
Habit cards with progress ring, progress %, and action buttons (+ / - / edit)
Modal for creating & editing habits
Export / Import controls and visual weekly chart

🚀 Getting Started

Prerequisites
Modern web browser (Chrome, Edge, Firefox, Safari)

Installation

Clone the repository

git clone https://github.com/your-username/habit-quest.git
cd habit-quest


Run Locally
Open index.html in your browser, or run a simple static server:

# Python 3
python -m http.server 8000
# Then open http://localhost:8000


📂 Project Structure

habit-quest/
├── index.html          # Main UI
├── style.css           # Cyberpunk glassmorphism styles
├── script.js           # App logic (points, habits, UI)
├── assets/             # (optional) icons, sounds, images
└── README.md           # Documentation


🎯 How to Use

Create Habit

Click New Habit (+)

Fill: name, daily goal, color, points per action, completion bonus

Save — habit appears as a card

Add Progress
• Click + on a habit card to log one action (gains defined points)
• Click − to undo last progress (deducts base points)
• When you hit the daily goal, a bonus is applied automatically

Profile & Levels
• Total Score shows cumulative XP
• Level is calculated from XP (1 level per 500 XP)
• Level progress bar shows progress to next level

Export / Import
• Click export to download a JSON backup
• Click import to upload a previously exported JSON

💻 Code Highlights (script.js)

SoundManager — lightweight WebAudio wrapper (tick, complete, level-up)

gain(id) — increments habit progress, awards points, handles bonus & sounds

getStreak(habit) — counts consecutive days done for streak badge

render() — dynamically builds habit cards with SVG ring & progress

saveData() / loadData() — persistence using localStorage

Import/Export: JSON read/write with validation

🔮 Future Enhancements

Cloud sync & account system (save across devices)

Push notifications / reminders

Achievements & badges (shareable certificates)

Social leaderboard & friend challenges

More analytics (monthly summaries, best streaks)

Mobile app wrapper (PWA / Electron)

🐛 Known Issues

Undo logic removes base points but may not fully roll back complex bonus state in edge cases.

localStorage limits sync to the same browser only (no cross-device support yet).

📝 Learning Outcomes
• Designing gamified UX with meaningful feedback
• Using Web Audio API for pleasing audio cues
• Building animated SVG and CSS-driven UI components
• Managing app state and persistence with localStorage
• Creating import/export flows and safe file parsing

👨‍💻 Author
Arjeet Kumar

GitHub: @Arjeetkumar
Project: 30 Days 30 Projects — Day 11

📄 License
This project is open source and free to use. (Add your preferred license, e.g., MIT.)

🙏 Acknowledgements
Design inspired by modern neon UI trends and glassmorphism.
Built with love and coffee during the 30 Days 30 Projects challenge.