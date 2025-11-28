# ⚡Premium Habit Quest — Cyberpunk Habit Tracker

A gamified, neon-themed habit tracker with XP, levels, streaks, animated progress rings, sound effects, import/export and beautiful glassmorphism UI. Built as Day 11 of the 30 Days 30 Projects challenge.

## Project Preview
<img width="1791" height="912" alt="Screenshot 2025-11-28 164412" src="https://github.com/user-attachments/assets/9111c6f5-fd0c-4de6-957a-203d4f731362" />

### ✨ Features
## 🎨 Design

- Cyberpunk Neon UI: Glassmorphism, glowing gradients, animated blobs and neon accents.
- Animated Progress Rings: SVG rings that animate on progress.
- Responsive Layout: Cards grid that adapts from desktop to mobile.
- Micro-interactions: Floating XP text, hover states, and level-up animations.

## 🔢 Functionality
- Gamified Points System: Points per action + completion bonus for daily goals.
- XP & Levels: Level up (every 500 XP by default) with celebration & sound.
- Streak Tracking: Consecutive-day streak detection.
- Create / Edit / Delete Habits: Custom name, daily goal, color, points, bonus.
- Undo Actions: Revert the last increment for a habit.
- Search Habits: Instant search to find habits quickly.
- Export / Import: Save or restore app data (.json) for backup or migration.
- Weekly Chart: View last 7 days of earned XP with tooltips.

## 🔊 Sound & Feedback
- Web Audio API: Tick sound for actions, multi-tone for completion, melody for level-up.
- Floating Notifications: +XP and LEVEL UP visual feedback.

## 💾 Persistence
- localStorage: Data saved locally (habits, profile, history).
- Safe Import/Export: JSON import with validation.

## 📱 UI Elements
- Top bar with total points, level & progress bar
- Habit cards with progress ring, progress %, and action buttons (+ / - / edit)
- Modal for creating & editing habits
- Export / Import controls and visual weekly chart

### git clone hhttps://github.com/Arjeetkumar/30-day-projects/edit/main/day11

## 📂 Project Structure

habit-quest/
├── index.html          # Main UI
├── style.css           # Cyberpunk glassmorphism styles
├── script.js           # App logic (points, habits, UI)
├── assets/             # (optional) icons, sounds, images
└── README.md           # Documentation

## 🔮 Future Enhancements

- Cloud sync & account system (save across devices)

- Push notifications / reminders

- Achievements & badges (shareable certificates)

- Social leaderboard & friend challenges

- More analytics (monthly summaries, best streaks)

- Mobile app wrapper (PWA / Electron)

## 🐛 Known Issues

- Undo logic removes base points but may not fully roll back complex bonus state in edge cases.

- localStorage limits sync to the same browser only (no cross-device support yet).

## 📝 Learning Outcomes
• Designing gamified UX with meaningful feedback
• Using Web Audio API for pleasing audio cues
• Building animated SVG and CSS-driven UI components
• Managing app state and persistence with localStorage
• Creating import/export flows and safe file parsing

## 👨‍💻 Author
### Arjeet Kumar

GitHub: @Arjeetkumar
Project: 30 Days 30 Projects — Day 11

