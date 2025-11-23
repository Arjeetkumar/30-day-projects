// --- DOM ELEMENTS ---
const audio = document.getElementById('audio');
const fileInput = document.getElementById('audioFile');
const canvas = document.getElementById('canvas');
const ctx = canvas.getContext('2d');
const lyricsDisplay = document.getElementById('lyricsDisplay');
const lyricsInput = document.getElementById('lyricsInput');
const glowSlider = document.getElementById('glowPower');
const textSlider = document.getElementById('textSize');

// --- STATE VARIABLES ---
let audioContext, analyser, dataArray;
let isInit = false;
let lyricsData = []; // Stores objects: { time: 12.5, text: "Lyrics..." }
let currentLine = "";

// --- RESIZE ---
function resize() {
    canvas.width = window.innerWidth - 320;
    canvas.height = window.innerHeight;
}
window.addEventListener('resize', resize);
resize();

// --- AUDIO SETUP ---
function initAudio() {
    if(isInit) return;
    const Actx = window.AudioContext || window.webkitAudioContext;
    audioContext = new Actx();
    const src = audioContext.createMediaElementSource(audio);
    analyser = audioContext.createAnalyser();
    analyser.fftSize = 256;
    src.connect(analyser);
    analyser.connect(audioContext.destination);
    dataArray = new Uint8Array(analyser.frequencyBinCount);
    isInit = true;
}

// --- PARSE LRC FUNCTION (THE MAGIC) ---
function parseLyrics(text) {
    const lines = text.split('\n');
    const result = [];
    
    // Regex to find [00:00.00] timestamps
    const timeRegex = /\[(\d{2}):(\d{2}\.?\d{0,3})\]/;

    lines.forEach(line => {
        const match = line.match(timeRegex);
        if (match) {
            // Convert "01:30.50" to seconds (90.5)
            const minutes = parseFloat(match[1]);
            const seconds = parseFloat(match[2]);
            const totalTime = (minutes * 60) + seconds;
            const lyricText = line.replace(timeRegex, '').trim(); // Remove time from text
            
            if(lyricText) {
                result.push({ time: totalTime, text: lyricText });
            }
        } else if (line.trim() !== "") {
            // Handle plain text lines (no timestamp)
            // Just add them with a slight delay from previous, or 0 if first
            const prevTime = result.length > 0 ? result[result.length-1].time + 3 : 0;
            result.push({ time: prevTime, text: line.trim() });
        }
    });
    
    return result;
}

// --- EVENT LISTENERS ---
fileInput.addEventListener('change', (e) => {
    const file = e.target.files[0];
    if(file){
        document.getElementById('fileName').innerText = file.name;
        audio.src = URL.createObjectURL(file);
        lyricsDisplay.innerText = "TRACK LOADED";
    }
});

document.getElementById('playBtn').addEventListener('click', () => {
    if(!isInit) initAudio();
    if(audioContext && audioContext.state === 'suspended') audioContext.resume();
    audio.play();
    animate();
});

document.getElementById('pauseBtn').addEventListener('click', () => audio.pause());

// APPLY LYRICS
document.getElementById('applyBtn').addEventListener('click', () => {
    const txt = lyricsInput.value;
    if(!txt) return;
    lyricsData = parseLyrics(txt);
    lyricsDisplay.innerText = "LYRICS SYNCED";
});

// DEMO SYNC (Generates example timestamped lyrics)
document.getElementById('aiBtn').addEventListener('click', () => {
    const demoLRC = 
`[00:01.00] Initializing System...
[00:04.00] Welcome to Neon Pulse
[00:08.00] This is how synced lyrics work
[00:12.00] You paste timestamps on the left
[00:16.00] And the code reads the audio time
[00:20.00] Enjoy the visualization!`;
    
    lyricsInput.value = demoLRC;
    lyricsData = parseLyrics(demoLRC);
    lyricsDisplay.innerText = "DEMO LOADED\nPRESS PLAY";
});

// Sliders
textSlider.addEventListener('input', (e) => lyricsDisplay.style.fontSize = e.target.value + "px");

// --- VISUALIZER LOOP ---
function animate() {
    if(audio.paused) return;
    requestAnimationFrame(animate);

    // 1. SYNC LYRICS LOGIC
    if(lyricsData.length > 0) {
        const currentTime = audio.currentTime;
        // Find the active line (current time is greater than lyric timestamp)
        // We look for the last lyric that has passed
        let activeLyric = lyricsData[0].text;
        
        for (let i = 0; i < lyricsData.length; i++) {
            if (currentTime >= lyricsData[i].time) {
                activeLyric = lyricsData[i].text;
            } else {
                break; // Stop looking if we passed current time
            }
        }
        
        // Only update DOM if text changed
        if(lyricsDisplay.innerText !== activeLyric) {
            lyricsDisplay.innerText = activeLyric;
        }
    }

    // 2. VISUALIZATION LOGIC
    analyser.getByteFrequencyData(dataArray);
    const w = canvas.width;
    const h = canvas.height;
    const cy = h / 2;
    const buffer = analyser.frequencyBinCount;

    ctx.clearRect(0,0,w,h);

    // Center Line
    ctx.beginPath();
    ctx.moveTo(0, cy);
    ctx.lineTo(w, cy);
    ctx.strokeStyle = "rgba(255,255,255,0.1)";
    ctx.stroke();

    let totalVol = 0;
    let bassVol = 0;
    const barWidth = (w / buffer) * 2;
    let x = 0;

    for(let i = 0; i < buffer; i++) {
        let val = dataArray[i];
        totalVol += val;
        if(i < 10) bassVol += val;

        let barH = val * 1.5;
        let r = val + 20;
        let g = 50;
        let b = 255;

        ctx.fillStyle = `rgb(${r}, ${g}, ${b})`;
        ctx.shadowBlur = 15;
        ctx.shadowColor = `rgba(${r}, ${g}, ${b}, 0.5)`;

        ctx.fillRect(x, cy - (barH / 2), barWidth, barH / 2);
        ctx.fillRect(x, cy, barWidth, barH / 2);

        ctx.shadowBlur = 0;
        x += barWidth + 2;
    }

    // 3. TEXT EFFECTS
    const bass = bassVol / 10;
    const glow = glowSlider.value;
    const scale = 1 + (bass / 800);
    
    lyricsDisplay.style.transform = `scale(${scale})`;
    lyricsDisplay.style.textShadow = `
        0 0 ${glow}px #00f3ff,
        0 0 ${glow*2}px #bc13fe,
        0 0 ${Math.max(0, bass-150)}px #ff0055
    `;
}