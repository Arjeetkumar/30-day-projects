🎨 FaceArt AI

A modern AI-powered face transformation tool with stunning visuals, seamless UI, and smart SDXL image-to-image generation. Built as Day 7 of the 30 Days 30 Projects Challenge.

FaceArt AI allows users to upload any portrait photo and transform it into Pixar, Cyberpunk, Anime, Sketch, Claymation, Zombie, or any custom art style using Stable Diffusion XL.

✨ Features
🎨 Design

Modern, glass-blur sidebar UI

Neon accent colors with premium aesthetics

Fully responsive and smooth animations

Clean preview area with compare mode

Loading overlay with “AI Dreaming” effect

🤖 AI Power

Image-to-Image transformation using SDXL (Stable Diffusion XL)

Smart auto-resizing to valid SDXL dimensions

Adjustable creativity slider (10%–90%)

Built-in style filters:

Pixar

Cyberpunk

Anime

Sketch

Zombie

Claymation

Optional custom prompt for full creativity

Instant result preview

Hold-to-compare button to quickly toggle original vs AI image

📸 Upload & Output

Upload any JPG/PNG photo

Automatically displayed in preview

AI output generated in PNG

One-click Download Result button

🚀 Getting Started
Prerequisites

Modern web browser (Chrome, Edge, Firefox, Safari)

Stability AI API key (SDXL Image-to-Image)

Installation

Clone the repository:

git clone https://github.com/yourusername/FaceArt-AI.git
cd FaceArt-AI


Run the project (no server needed):
Simply open:

index.html

📂 Project Structure
FaceArt-AI/
├── index.html          # Main UI structure
├── style.css           # Neon UI, glass sidebar, transitions
├── script.js           # AI logic, API call, auto resizing, UI handling
├── assets/             # Optional: icons, backgrounds
└── README.md           # Documentation

🎯 How to Use
1. Upload Photo

Click 📸 Choose Photo

Select an image (preferably a face)

2. Select a Style

Choose one filter from:

Pixar • Anime • Cyberpunk • Sketch • Zombie • Clay

3. Adjust AI Strength

10–30% → subtle edit

40–60% → balanced transformation

70–90% → dramatic restyle

4. Optional Custom Prompt

Add extra instructions like:

neon lighting, cinematic shading, 4k ultra detail

5. Generate

Click ✨ Generate AI Art

6. Preview

Output appears instantly

Press & hold Hold to Compare to toggle original → AI result

7. Download

Click ⬇ Save Image to download your AI-generated art.

💻 Code Highlights
🖼 Smart Auto-Resize (SDXL Required)

SDXL only accepts 9 specific resolutions.
This tool automatically finds the closest valid dimension:

function getClosestDimension(width, height) {
    const aspectRatio = width / height;
    let bestMatch = ALLOWED_DIMENSIONS[0];
    ...
}

🔄 Original vs AI Compare Feature
compareBtn.addEventListener('mousedown', () => {
    resultImage.src = originalImageURL;
});
compareBtn.addEventListener('mouseup', () => {
    resultImage.src = aiResultURL;
});

🔥 AI Request (Stable Diffusion XL)
formData.append('init_image', resizedBlob);
formData.append('text_prompts[0][text]', finalPrompt);
formData.append('image_strength', 1 - strength);

🎨 Styling Details
Color Palette
Use	Color
Accent	#ff0055 (Neon Pink)
Accent Gradient	Pink → Gold
Background	#0f0c29 dark gradient
Sidebar	Semi-transparent glass blur
UI Components:

Glassy neon buttons

Dynamic shadows and glow

Smooth hover effects

Blurred glass sidebar

🔮 Future Enhancements

Background remover + custom scene

Change-gender, old-age, child-face filters

Live camera mode

HD upscale option

Color-grading presets

Face anonymization AI

AI animations / video output (future)

🐛 Known Issues

Very large images take longer to resize

Some styles may alter facial identity too much at high strength

API key must be manually added in script.js (insecure for production)

📝 Learning Outcomes

This project helped practice:

Working with AI Image APIs (Stability AI)

Image resizing + canvas manipulation

Advanced UI/UX design with glassmorphism

Handling Blobs, base64 conversion, and async file operations

Creating dynamic sliders, filters, prompt builders

Deep understanding of Image-to-Image AI workflows

Building a complete web-app with no backend

👨‍💻 Author

Arjeet Kumar
IIT Patna – BSc CS & Data Analysis
Day 7 – 30 Days 30 Projects Challenge