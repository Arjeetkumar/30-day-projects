# 🎵 Neon Lyrics Visualizer

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
