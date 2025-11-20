🌟 Daily Affirmation Viewer

A beautifully designed desktop affirmation viewer that displays uplifting images, motivational text, and plays soft sound effects — all while tracking your progress with a gamified points system.
Built as Day 4 of the 30 Days 30 Projects challenge by Arjeet Kumar.

Affirmation Viewer Preview
(Add your screenshot here)

✨ Features
🎨 Design & UI

Clean, minimal dark-themed UI

Smooth auto-scaling of images

Centered canvas display with dynamic resizing

Soft caption overlay with motivational quotes

Progress indicator dots (up to 20 images)

Beautiful button layout with modern styling

🖼️ Image Features

Auto-loads all images from /images/ folder

Supports: PNG, JPG, JPEG, GIF, BMP, WEBP

Auto-resizes images to fit the window

Smart detection of missing/broken images

Shuffle mode for random inspiration

Favorite any image (saved to /favorites/)

Export your favorites as a ZIP file

⏱️ Slideshow Features

Auto-slide every X seconds (default: 3s)

Adjustable interval via UI

Keyboard shortcuts:

⏩ Right Arrow → Next image

⏪ Left Arrow → Previous image

⏯ Space → Play / Pause

🔀 S → Shuffle on/off

📺 F → Fullscreen toggle

➕ / ➖ → Increase/decrease interval

📥 N → Add new images

🔊 Sound System

Plays sound.mp3 on each slide transition

Runs sound in a non-blocking background thread

Works automatically if pygame is installed

📝 Captions System

Reads quotes from captions.txt

Supports:

"filename.png | Your caption" (specific caption)

"Just a positive affirmation" (generic pool)

Displays captions under each affirmation image

🎮 Gamification — Points & Levels

A fun way to stay motivated!

You earn:

+1 point for viewing each new affirmation

+10 points for marking favorites

Automatic level-up every 100 points

Displayed in the UI:

⭐ Points

🥇 Level

Progress is saved in settings.json

🚀 Getting Started
🔧 Prerequisites

Python 3.x

Install dependencies:

pip install pillow pygame

📂 Folder Structure
day4/
├── affirmation_viewer.py    # Main application
├── images/                  # Add your affirmation images here
├── favorites/               # Saved favorite images
├── captions.txt             # Captions for images
├── settings.json            # Auto-generated user settings
└── sound.mp3                # Slide transition sound

▶️ Running the App
python affirmation_viewer.py

📂 Project Structure (Detailed)

affirmation_viewer.py
Full application logic (UI, slideshow, favorites, captions, sound, points)

images/
Put all your affirmation photos here.

favorites/
Auto-created. Stores images you mark as Favorite.

sound.mp3
Small motivational audio clip played on every slide.

captions.txt
Format:

image1.png | Believe in yourself.
image2.jpg | You are unstoppable.
Every day is a new chance.


You can mix both formats.

settings.json
Stores:

interval

shuffle

last_index

points

level

💡 Code Highlights
🎞️ Smart Image Scaling

Automatically adapts image size to the window with aspect-ratio preservation.

🧠 Intelligent Shuffle System

Remembers last viewed image, even after shuffling.

💾 Persistent State

Your preferences + profile + last index saved automatically on close.

🎵 Non-blocking Sound Playback

Ensures smooth UI even while playing audio.

⭐ Gamified User Experience

Points & levels make the viewer fun and habit-building.

🐛 Known Issues

Very long captions may overflow on extremely small windows

GIF animations currently show first frame (Tkinter limitation)

Sound requires pygame installed — otherwise skipped silently

🔮 Future Enhancements

Add background music mode

Add "Daily Streak" tracker

Add category folders inside /images

Add transitions: fade, slide-in

Add image filters (warmth, glow, brightness)

Add drag-and-drop image import

🧠 Learning Outcomes

This project helped practice:

Tkinter canvas & UI layout

Image processing with Pillow (PIL)

Non-blocking sound threads

File system operations & persistence

Gamification logic (points & leveling)

Designing clean, modern desktop apps

👨‍💻 Author

Arjeet Kumar
30 Days 30 Projects Challenge
GitHub: @Arjeetkumar