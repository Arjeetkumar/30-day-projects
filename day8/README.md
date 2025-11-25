🌤️ WeatherGlow – Premium Weather Dashboard

A modern, futuristic, and beautifully designed glass-UI weather application featuring live weather data, 5-day forecasts, floating aurora animations, and a responsive dashboard layout.
Built as Day 8 of my 30 Days 30 Projects Challenge.

🖼️ Project Preview

(Add this screenshot in your repo)

👉 You can upload:
/mnt/data/IMG-20250216-WA0032.jpg

✨ Features
🎨 Design & UI

Elegant Glassmorphism UI with soft frosted cards

Animated Aurora / Neon Blobs Background

Responsive 2-column dashboard layout

Lucide icons for clean and modern visuals

Smooth hover transitions & card animations

Dynamic icons for sunny, rainy, snowy, foggy, and thunder weather

Auto-adapting forecast cards with gentle motion

🌦️ Weather Features
Current Weather Panel

Live temperature

Weather condition (Clear, Rain, Snow, Fog etc.)

Dynamic weather icon based on day/night

High/low temp for today

City name & date display

Weather Details

Wind Speed

Humidity

Air Pressure

Visibility estimation

Cloud-cover-based clarity indicator

Forecast System

5-Day weather forecast

Day-wise temperatures

Independent weather icons

Smooth hover highlight animations

🔍 Smart Search System

Type a city and press Enter

Autoloads weather via Open-Meteo Geocoding API

Saves last searched city in localStorage

Loads previous city automatically on startup

⚙️ Tech Used

HTML5 – UI structure

CSS3 (Glassmorphism + animations)

JavaScript (ES6) – logic, API handling

Lucide Icons

Open-Meteo APIs

Geocoding API

Forecast API

🚀 Getting Started
Prerequisites

Any modern browser

VS Code / local server (optional)

Run Locally
git clone https://github.com/<your-username>/<your-repo>.git
cd your-project-folder


Open directly:

index.html


Or run local server:

# Python 3
python -m http.server 8000

📂 Project Structure
weather-app/
├── index.html         # Main UI structure
├── style.css          # Glass UI + Aurora effects
├── script.js          # Weather logic + API + forecast
├── assets/
│   ├── icons/         # Optional custom icons
│   └── images/        # Banner/screenshot
└── README.md          # Documentation

🎯 How It Works
🔹 1. City Search

Enter a city → App fetches coordinates → Loads weather.

🔹 2. Weather API

Uses Open-Meteo to fetch:

Current temperature

Weather codes

Max/min temps

Humidity, wind, pressure, cloud cover

🔹 3. Dynamic Icons

Weather code → mapped to lucide icon

🔹 4. Forecast

Renders 5-day data dynamically using template injection.

🔹 5. UI Animations

Aurora blobs float infinitely using keyframes.

💻 Code Highlights
⭐ Smart Weather Icon Mapping
function getWeatherIcon(code, isDay) {
    if (code === 0) return isDay ? "sun" : "moon";
    if ([1,2,3].includes(code)) return isDay ? "cloud-sun" : "cloud-moon";
    if ([45,48].includes(code)) return "cloud-fog";
    if ([51,61,63,80].includes(code)) return "cloud-rain";
    if ([71,73,75,77].includes(code)) return "snowflake";
    if ([95,96,99].includes(code)) return "cloud-lightning";
    return "cloud";
}

⭐ Dynamic Forecast Rendering
const item = `
  <div class="forecast-item">
    <span class="forecast-day">${dayName}</span>
    <div class="forecast-icon"><i data-lucide="${icon}"></i></div>
    <span class="forecast-temp">${max}° <span>${min}°</span></span>
  </div>
`;

⭐ Aurora Animation
@keyframes float {
  0%,100% { transform: scale(1); }
  33%     { transform: translate(30px, -50px) scale(1.1); }
  66%     { transform: translate(-20px, 20px) scale(0.9); }
}

🔮 Future Enhancements

🌙 Dark/Light mode automatic switching

🌅 Dynamic background based on sunrise/sunset

📍 Auto-detect location using GPS

📈 Hourly graph with charts.js

🌡️ Temperature unit toggle (°C / °F)

🔔 Weather alerts notifications

🎨 Custom theme colors

🐛 Known Issues

Visibility uses cloud-cover estimation (API limitation)

Forecast icons always show “day” version

Searching extremely rare cities may fail occasionally

Open-Meteo API sometimes gives timezone delay

📝 Learning Outcomes

This project helped me master:

API integration & async workflows

Modern dashboard layout with CSS Grid

Glassmorphism & neon design aesthetics

DOM manipulation at scale

Weather code systems (WMO)

LocalStorage usage

Search-UX design

Animation performance optimization

👨‍💻 Author

Arjeet Kumar
30 Days 30 Projects Challenge
💙 Crafting UI, Logic & Real-World Mini-Apps