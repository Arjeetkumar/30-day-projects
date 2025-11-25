// --- CONFIG ---
const DEFAULT_CITY = "Patna";
const GEO_API = "https://geocoding-api.open-meteo.com/v1/search";
const WEATHER_API = "https://api.open-meteo.com/v1/forecast";

// --- DOM ELEMENTS ---
const cityInput = document.getElementById('cityInput');
const cityNameEl = document.getElementById('cityName');
const currentDateEl = document.getElementById('currentDate');
const currentTempEl = document.getElementById('currentTemp');
const weatherDescEl = document.getElementById('weatherDesc');
const weatherIconEl = document.getElementById('weatherIcon');
const maxTempEl = document.getElementById('maxTemp');
const minTempEl = document.getElementById('minTemp');

const windSpeedEl = document.getElementById('windSpeed');
const humidityEl = document.getElementById('humidity');
const visibilityEl = document.getElementById('visibility');
const pressureEl = document.getElementById('pressure');
const forecastListEl = document.getElementById('forecastList');

// --- INITIALIZATION ---
document.addEventListener('DOMContentLoaded', () => {
    lucide.createIcons();
    
    // Set Date
    const options = { weekday: 'long', month: 'short', day: 'numeric' };
    currentDateEl.innerText = new Date().toLocaleDateString('en-US', options);

    // Load Weather
    const savedCity = localStorage.getItem('weather_city') || DEFAULT_CITY;
    fetchWeather(savedCity);
});

// --- SEARCH LISTENER ---
cityInput.addEventListener('keypress', (e) => {
    if (e.key === 'Enter') {
        const city = cityInput.value.trim();
        if (city) {
            fetchWeather(city);
            cityInput.value = '';
            cityInput.blur();
        }
    }
});

// --- FETCH LOGIC ---
async function fetchWeather(city) {
    try {
        // 1. Get Lat/Lon for City
        const geoRes = await fetch(`${GEO_API}?name=${city}&count=1&language=en&format=json`);
        const geoData = await geoRes.json();

        if (!geoData.results) {
            alert("City not found!");
            return;
        }

        const { latitude, longitude, name, timezone } = geoData.results[0];
        cityNameEl.innerText = name;
        localStorage.setItem('weather_city', name);

        // 2. Get Weather Data
        const weatherUrl = `${WEATHER_API}?latitude=${latitude}&longitude=${longitude}&current=temperature_2m,relative_humidity_2m,is_day,precipitation,rain,showers,snowfall,weather_code,cloud_cover,pressure_msl,surface_pressure,wind_speed_10m&daily=weather_code,temperature_2m_max,temperature_2m_min&timezone=auto`;
        
        const weatherRes = await fetch(weatherUrl);
        const weatherData = await weatherRes.json();

        updateUI(weatherData);

    } catch (error) {
        console.error("Error fetching weather:", error);
        cityNameEl.innerText = "Error";
    }
}

// --- UI UPDATE ---
function updateUI(data) {
    const current = data.current;
    const daily = data.daily;

    // Current Weather
    currentTempEl.innerText = `${Math.round(current.temperature_2m)}°`;
    weatherDescEl.innerText = getWeatherDescription(current.weather_code);
    
    // Update Icon based on code + is_day
    const iconName = getWeatherIcon(current.weather_code, current.is_day);
    weatherIconEl.innerHTML = `<i data-lucide="${iconName}"></i>`;

    // High/Low (from daily[0] which is today)
    maxTempEl.innerText = `${Math.round(daily.temperature_2m_max[0])}°`;
    minTempEl.innerText = `${Math.round(daily.temperature_2m_min[0])}°`;

    // Details
    windSpeedEl.innerHTML = `${current.wind_speed_10m} <span>km/h</span>`;
    humidityEl.innerHTML = `${current.relative_humidity_2m} <span>%</span>`;
    pressureEl.innerHTML = `${current.surface_pressure} <span>hPa</span>`;
    
    // Visibility is not directly in Open-Meteo free tier easily, simulating or using cloud cover as proxy for "clarity"
    // Let's use Cloud Cover inverse as a proxy for "Visibility" score for now or just static for demo
    const visibility = current.cloud_cover < 20 ? "10+" : (10 - (current.cloud_cover/10)).toFixed(1);
    visibilityEl.innerHTML = `${visibility} <span>km</span>`;

    // Forecast (Next 5 days)
    renderForecast(daily);

    // Re-init icons
    lucide.createIcons();
}

function renderForecast(daily) {
    forecastListEl.innerHTML = '';
    
    // Open-Meteo returns 7 days usually. We take next 5 (skip index 0 as it is today)
    for(let i = 1; i <= 5; i++) {
        const date = new Date(daily.time[i]);
        const dayName = date.toLocaleDateString('en-US', { weekday: 'short' });
        const code = daily.weather_code[i];
        const max = Math.round(daily.temperature_2m_max[i]);
        const min = Math.round(daily.temperature_2m_min[i]);
        const icon = getWeatherIcon(code, 1); // Always use day icon for forecast

        const item = `
            <div class="forecast-item">
                <span class="forecast-day">${dayName}</span>
                <div class="forecast-icon"><i data-lucide="${icon}"></i></div>
                <span class="forecast-temp">${max}° <span>${min}°</span></span>
            </div>
        `;
        forecastListEl.innerHTML += item;
    }
}

// --- HELPERS ---
// WMO Weather Codes to Description & Icon
function getWeatherDescription(code) {
    const codes = {
        0: "Clear Sky",
        1: "Mainly Clear", 2: "Partly Cloudy", 3: "Overcast",
        45: "Fog", 48: "Depositing Rime Fog",
        51: "Light Drizzle", 53: "Moderate Drizzle", 55: "Dense Drizzle",
        61: "Slight Rain", 63: "Moderate Rain", 65: "Heavy Rain",
        71: "Slight Snow", 73: "Moderate Snow", 75: "Heavy Snow",
        77: "Snow Grains",
        80: "Slight Showers", 81: "Moderate Showers", 82: "Violent Showers",
        95: "Thunderstorm", 96: "Thunderstorm & Hail"
    };
    return codes[code] || "Unknown";
}

function getWeatherIcon(code, isDay) {
    // Map codes to Lucide icon names
    // 0 = Clear
    if (code === 0) return isDay ? "sun" : "moon";
    
    // 1,2,3 = Cloudy
    if ([1, 2, 3].includes(code)) return isDay ? "cloud-sun" : "cloud-moon";
    
    // 45,48 = Fog
    if ([45, 48].includes(code)) return "cloud-fog";
    
    // 51-67 = Rain/Drizzle
    if ([51, 53, 55, 61, 63, 65, 80, 81, 82].includes(code)) return "cloud-rain";
    
    // 71-77 = Snow
    if ([71, 73, 75, 77, 85, 86].includes(code)) return "snowflake";
    
    // 95-99 = Thunder
    if ([95, 96, 99].includes(code)) return "cloud-lightning";

    return "cloud";
}