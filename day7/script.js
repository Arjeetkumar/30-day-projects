// API Key (Hardcoded for simplicity; in production, use secure storage)
const API_KEY = "sk-KCQQuTCIHyqsBRHfvXHNxw0DzYKnukm32FQmwtUvWf2F7K91";

// DOM Elements
const uploadInput = document.getElementById('uploadInput');
const resultImage = document.getElementById('resultImage');
const placeholder = document.getElementById('placeholder');
const loading = document.getElementById('loading');
const compareBtn = document.getElementById('compareBtn');
const strengthSlider = document.getElementById('aiStrength');
const strengthValue = document.getElementById('strengthValue');
const customPrompt = document.getElementById('customPrompt');

// State
let originalFile = null;
let originalImageURL = "";
let currentFilterPrompt = "";
let currentFilterName = "";

// SDXL Allowed Dimensions (Must use one of these)
const ALLOWED_DIMENSIONS = [
    { w: 1024, h: 1024 }, // 1:1 Square
    { w: 1152, h: 896 },  // Landscape
    { w: 1216, h: 832 },  // Landscape Wide
    { w: 1344, h: 768 },  // Landscape Wider (Closest to 720p)
    { w: 1536, h: 640 },  // Landscape Panoramic
    { w: 640, h: 1536 },  // Portrait Panoramic
    { w: 768, h: 1344 },  // Portrait Tall
    { w: 832, h: 1216 },  // Portrait
    { w: 896, h: 1152 }   // Portrait
];

// --- 1. UPLOAD HANDLING ---
uploadInput.addEventListener('change', (e) => {
    const file = e.target.files[0];
    if (!file) return;
    
    originalFile = file;
    
    // Preview Logic
    originalImageURL = URL.createObjectURL(file);
    resultImage.src = originalImageURL;
    resultImage.style.display = 'block';
    placeholder.style.display = 'none';
    compareBtn.style.display = 'none';
});

// --- 2. UI UPDATES ---
strengthSlider.addEventListener('input', (e) => {
    strengthValue.innerText = e.target.value + "%";
});

function setFilter(style) {
    document.querySelectorAll('.filter-grid button').forEach(b => b.classList.remove('active'));
    event.target.classList.add('active');

    const prompts = {
        'toon': "pixar style, disney 3d render, cute, smooth, vibrant, high detail, unreal engine 5",
        'cyberpunk': "cyberpunk character, neon lights, mechanical implants, futuristic city, scifi, high contrast",
        'anime': "studio ghibli style, anime character, vibrant, cel shaded, highly detailed, japanese art",
        'sketch': "charcoal sketch, pencil drawing, rough lines, artistic, black and white, paper texture",
        'zombie': "scary zombie, rotting skin, horror, cinematic lighting, walking dead style, dark",
        'clay': "claymation style, stop motion, plasticine, aardman style, playdough texture"
    };
    currentFilterPrompt = prompts[style];
    currentFilterName = style;
}

// --- 3. SMART RESIZING LOGIC (The Fix) ---
function getClosestDimension(width, height) {
    const aspectRatio = width / height;
    
    // Find the allowed dimension with the closest aspect ratio
    let bestMatch = ALLOWED_DIMENSIONS[0];
    let minDiff = 999;

    ALLOWED_DIMENSIONS.forEach(dim => {
        const dimRatio = dim.w / dim.h;
        const diff = Math.abs(aspectRatio - dimRatio);
        if (diff < minDiff) {
            minDiff = diff;
            bestMatch = dim;
        }
    });

    console.log(`Original: ${width}x${height}, Resizing to: ${bestMatch.w}x${bestMatch.h}`);
    return bestMatch;
}

function resizeImage(file) {
    return new Promise((resolve) => {
        const img = new Image();
        img.src = URL.createObjectURL(file);
        img.onload = () => {
            const target = getClosestDimension(img.width, img.height);
            
            const canvas = document.createElement('canvas');
            canvas.width = target.w;
            canvas.height = target.h;
            const ctx = canvas.getContext('2d');
            
            // Draw and resize image to fit the valid API dimensions
            ctx.drawImage(img, 0, 0, target.w, target.h);
            
            // Convert back to Blob (File)
            canvas.toBlob((blob) => {
                resolve(blob);
            }, 'image/png');
        };
    });
}

// --- 4. GENERATE AI ---
async function generateAI() {
    if (!originalFile) return alert("⚠️ Please upload an image first!");
    if (!currentFilterPrompt && !customPrompt.value) return alert("⚠️ Please select a style!");

    loading.style.display = 'flex';

    try {
        // Step A: Resize the image to valid SDXL dimensions
        const resizedBlob = await resizeImage(originalFile);

        // Step B: Prepare Data
        const finalPrompt = `${currentFilterPrompt || ""} ${customPrompt.value || ""}`.trim();
        const strength = parseFloat(strengthSlider.value) / 100;

        const formData = new FormData();
        formData.append('init_image', resizedBlob); // Send resized image
        formData.append('init_image_mode', 'IMAGE_STRENGTH');
        formData.append('image_strength', 1 - strength); 
        formData.append('text_prompts[0][text]', finalPrompt);
        formData.append('cfg_scale', 7);
        formData.append('samples', 1);
        formData.append('steps', 30);

        // Step C: Call API
        const response = await fetch('https://api.stability.ai/v1/generation/stable-diffusion-xl-1024-v1-0/image-to-image', {
            method: 'POST',
            headers: {
                'Authorization': `Bearer ${API_KEY}`, // Using hardcoded key
                'Accept': 'application/json'
            },
            body: formData
        });

        const data = await response.json();

        if (!response.ok) {
            throw new Error(data.message || JSON.stringify(data));
        }

        const base64Image = data.artifacts[0].base64;
        resultImage.src = `data:image/png;base64,${base64Image}`;
        compareBtn.style.display = 'block';

    } catch (error) {
        console.error(error);
        alert("❌ Error: " + error.message);
    } finally {
        loading.style.display = 'none';
    }
}

// --- 5. UTILITIES ---
let aiResultURL = "";
const observer = new MutationObserver(() => {
    if (resultImage.src.startsWith('data:')) aiResultURL = resultImage.src;
});
observer.observe(resultImage, { attributes: true, attributeFilter: ['src'] });

compareBtn.addEventListener('mousedown', () => { resultImage.src = originalImageURL; });
compareBtn.addEventListener('mouseup', () => { if(aiResultURL) resultImage.src = aiResultURL; });
compareBtn.addEventListener('touchstart', () => { resultImage.src = originalImageURL; });
compareBtn.addEventListener('touchend', () => { if(aiResultURL) resultImage.src = aiResultURL; });

function downloadImage() {
    if (!resultImage.src) return;
    const link = document.createElement('a');
    link.download = `facetoon-${currentFilterName || 'edit'}.png`;
    link.href = resultImage.src;
    link.click();
}