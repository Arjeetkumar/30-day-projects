🎵 Neon Lyrics Visualizer

A futuristic, cyberpunk-inspired music visualizer with synced lyrics (LRC), glowing audio bars, neon animations, and a fully responsive hologram-style UI.
Built as Day 6 of the 30 Days, 30 Projects challenge.

🎬 Preview (UI Overview)

A modern neon interface featuring:

Holographic lyric panel

Bass-reactive glow

Mirror waveform bars

Cyberpunk glass sidebar

Smooth animations

Real-time lyric syncing

✨ Features
🎨 Design

Cyberpunk HUD UI

Glassmorphism Sidebar

Neon Glow Effects (Cyan + Purple + Pink)

Responsive Layout

Animated Waveform Canvas

Futuristic Fonts (Orbitron, Rajdhani)

Smooth transitions on text + panels

🎵 Audio Features

Upload any MP3 file instantly

AudioContext (Web Audio API) powered analyzer

Real-time frequency bars

Dual-wave mirror effect (Top + Bottom bars)

Beat detection → auto text scaling

📝 Lyrics Features

Supports LRC Timestamped Lyrics like Spotify / YouTube Music

Example format:

[00:12.50] Line 1 here
[00:15.80] Another synced line


Auto-synchronizes each lyric line with the audio timestamp

Smooth lyric transitions

Auto-detects lines even without timestamps

AI Demo button for auto-generated sample synced lyrics

✍️ Text Controls

Adjustable text size

Adjustable glow intensity

Dynamic neon pulse based on bass

🕹️ Controls

Play / Pause buttons

Load MP3

Load Lyrics

Demo Mode

Fully keyboard-safe and responsive

🚀 Getting Started
Prerequisites

Any modern browser:
Chrome, Firefox, Edge, Brave ✔

No backend required

Works fully offline

🛠 Installation

Clone or download this project:

git clone https://github.com/yourusername/neon-lyrics-visualizer.git
cd neon-lyrics-visualizer


Open directly:

index.html


Or run a local server:

python -m http.server 8000


Then open:

http://localhost:8000

📂 Project Structure
NeonVisualizer/
│
├── index.html        # Main HTML structure
├── style.css         # UI styling (neon + glassmorphism)
├── script.js         # Visualizer logic + LRC syncing
├── assets/           # (Optional) Backgrounds, icons, UI extras
└── README.md         # Documentation (this file)

🎯 How to Use
1. Upload MP3

Click “Upload MP3”

Select any audio file

Audio loads instantly

2. Add Lyrics

Paste timestamped lyrics (LRC format)

Example:

[00:01.00] Welcome to Neon Pulse
[00:05.50] Lyrics synced with audio

3. Play Music

Hit the Play button

Watch:

Neon bars animate

Lyrics change on time

Glow intensity react to bass

4. Customize

Drag Text Size slider

Drag Glow Power slider

Load demo lyrics

💻 Code Highlights
1. LRC Parser

Extracts time + text automatically:

const timeRegex = /\[(\d{2}):(\d{2}\.?\d{0,3})\]/;

2. Audio Visualizer Bars

Using Web Audio API:

analyser.getByteFrequencyData(dataArray);
ctx.fillRect(x, cy - barH/2, barWidth, barH);

3. Syncing Lyrics With Audio

Perfect match with audio.currentTime:

if (currentTime >= lyricsData[i].time) {
    activeLyric = lyricsData[i].text;
}

4. Neon Pulse Effect
lyricsDisplay.style.transform = `scale(${1 + bass / 800})`;

🎨 Styling Details
Color Palette

Cyan (Primary): #00f3ff

Purple (Secondary): #bc13fe

Neon Pink (Accent): #ff0055

Dark Background: #050510

Glow Shadows

Text & bars have layered glow:

text-shadow: 
   0 0 20px var(--primary),
   0 0 40px var(--secondary);

Glass Sidebar
backdrop-filter: blur(20px);
background: rgba(255,255,255,0.05);

📱 Responsive Design

Works well on:

Desktop

Wide screens

Tablets (landscape)

Mobile support limited due to Audio API restrictions.

🔮 Future Enhancements

Karaoke word-by-word highlight

Auto lyric sync (AI beats detection)

Multiple visualization modes

Circular hologram waveform

Background particle effects

Import external LRC files

Dark/Light neon color themes

🐛 Known Issues

Some mobile browsers restrict AudioContext

Large MP3 files may cause slight visual lag

Missing LRC timestamps → fallback uses auto timing

📝 Learning Outcomes

This project teaches:

Web Audio API

Canvas API

LRC format parsing

State management

DOM animation

Cyberpunk UI design

Glow / neon / glassmorphism effects

Modular JS logic

Event-driven programming in JS

👨‍💻 Author

Made by Arjeet
From the 30 Days — 30 Projects Challenge