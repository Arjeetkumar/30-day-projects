// script.js — Simple Pomodoro web app (no build tools)
// Persist state in localStorage under key 'pomodoro_state'
// Keyboard: Space start/pause, R reset, S skip, L manual log

const STATE_KEY = 'pomodoro_state_v1';

const defaultState = {
  workMin: 25,
  shortMin: 5,
  longMin: 15,
  cyclesBeforeLong: 4,
  pomodorosToday: 0,
  date: (new Date()).toISOString().slice(0,10),
  voice: false
};

let state = loadState();
let mode = 'Work'; // 'Work' | 'Short Break' | 'Long Break'
let remaining = state.workMin * 60;
let isRunning = false;
let completedCycles = 0;
let timerInterval = null;

// DOM
const timerText = document.getElementById('timerText');
const modeLabel = document.getElementById('modeLabel');
const startBtn = document.getElementById('startBtn');
const pauseBtn = document.getElementById('pauseBtn');
const resetBtn = document.getElementById('resetBtn');
const skipBtn = document.getElementById('skipBtn');
const countEl = document.getElementById('count');
const progressText = document.getElementById('progressText');
const statusEl = document.getElementById('status');
const alarmAudio = document.getElementById('alarmAudio');
const rainAudio = document.getElementById('rainAudio');
const rainToggle = document.getElementById('rainToggle');
const settingsBtn = document.getElementById('settingsBtn');
const settingsModal = document.getElementById('settingsModal');
const saveSettings = document.getElementById('saveSettings');
const closeSettings = document.getElementById('closeSettings');

const workInput = document.getElementById('workInput');
const shortInput = document.getElementById('shortInput');
const longInput = document.getElementById('longInput');
const cyclesInput = document.getElementById('cyclesInput');
const voiceToggle = document.getElementById('voiceToggle');

const progressCircle = document.querySelector('.progress-ring__circle');
const RADIUS = 96;
const CIRCUMFERENCE = 2 * Math.PI * RADIUS;
progressCircle.style.strokeDasharray = `${CIRCUMFERENCE}`;

function loadState(){
  try{
    const raw = localStorage.getItem(STATE_KEY);
    if(raw){
      const s = JSON.parse(raw);
      // reset daily count if date changed
      const today = (new Date()).toISOString().slice(0,10);
      if(s.date !== today){ s.pomodorosToday = 0; s.date = today; }
      return Object.assign({}, defaultState, s);
    }
  }catch(e){
    console.warn('load state error', e);
  }
  return Object.assign({}, defaultState);
}

function saveState(){
  try{
    localStorage.setItem(STATE_KEY, JSON.stringify(state));
  }catch(e){ console.warn('save state', e); }
}

function setTimerFromState(){
  if(mode === 'Work') remaining = state.workMin * 60;
  else if(mode === 'Short Break') remaining = state.shortMin * 60;
  else remaining = state.longMin * 60;
}

function formatTime(sec){
  const m = Math.floor(sec/60);
  const s = sec % 60;
  return `${String(m).padStart(2,'0')}:${String(s).padStart(2,'0')}`;
}

function updateUI(){
  timerText.textContent = formatTime(remaining);
  modeLabel.textContent = mode;
  countEl.textContent = state.pomodorosToday;
  statusEl.textContent = isRunning ? `${mode} — Running` : 'Ready';
  // progress percent in current session
  let total = (mode === 'Work') ? state.workMin*60 : (mode === 'Short Break' ? state.shortMin*60 : state.longMin*60);
  const pct = total ? Math.round((1 - (remaining/total)) * 100) : 0;
  progressText.textContent = `${Math.min(100,pct)}%`;
  // update ring stroke
  const offset = CIRCUMFERENCE - (pct/100) * CIRCUMFERENCE;
  progressCircle.style.strokeDashoffset = offset;
  // buttons
  startBtn.disabled = isRunning;
  pauseBtn.disabled = !isRunning;
}

function startTimer(){
  if(isRunning) return;
  isRunning = true;
  updateUI();
  timerInterval = setInterval(()=>{
    if(remaining > 0){
      remaining--;
      updateUI();
    } else {
      clearInterval(timerInterval);
      isRunning = false;
      onSessionComplete();
    }
  }, 1000);
}

function pauseTimer(){
  if(!isRunning) return;
  isRunning = false;
  clearInterval(timerInterval);
  updateUI();
}

function resetTimer(){
  pauseTimer();
  setTimerFromState();
  updateUI();
  stopAlarm();
}

function skipSession(){
  pauseTimer();
  onSessionComplete(true);
}

function manualLog(){
  state.pomodorosToday = (state.pomodorosToday || 0) + 1;
  saveState();
  updateUI();
}

function playAlarm(){
  if(alarmAudio && alarmAudio.src){
    alarmAudio.currentTime = 0;
    alarmAudio.play().catch(()=>{ beepFallback(); });
  } else {
    beepFallback();
  }
}

function stopAlarm(){
  try{ if(alarmAudio) alarmAudio.pause(), alarmAudio.currentTime=0; } catch(e){}
}

function beepFallback(){
  try{
    const ctx = new (window.AudioContext || window.webkitAudioContext)();
    const o = ctx.createOscillator();
    const g = ctx.createGain();
    o.type = 'sine';
    o.frequency.value = 880;
    o.connect(g); g.connect(ctx.destination);
    o.start();
    g.gain.exponentialRampToValueAtTime(0.00001, ctx.currentTime + 1.0);
    setTimeout(()=>{ o.stop(); }, 1100);
  }catch(e){ console.warn('beep fallback failed', e); }
}

function onSessionComplete(skipped=false){
  // if work ended and not skipped -> increment count
  if(mode === 'Work' && !skipped){
    state.pomodorosToday = (state.pomodorosToday || 0) + 1;
    saveState();
  }
  // alarm + optional voice
  playAlarm();
  if(state.voice){
    try{
      const msg = mode === 'Work' ? 'Work session finished. Take a break.' : 'Break finished. Time to work.';
      const ut = new SpeechSynthesisUtterance(msg);
      speechSynthesis.speak(ut);
    }catch(e){}
  }
  // small delay so alarm plays then show confirm
  setTimeout(()=>{
    stopAlarm();
    alert(`${mode} finished!`);
  }, 300);
  // advance mode
  if(mode === 'Work'){
    completedCycles++;
    if(completedCycles % state.cyclesBeforeLong === 0){
      mode = 'Long Break';
    } else {
      mode = 'Short Break';
    }
  } else {
    // break ended -> go to work
    mode = 'Work';
  }
  setTimerFromState();
  updateUI();
}

function toggleRain(){
  if(rainAudio && rainAudio.src){
    if(rainAudio.paused){
      rainAudio.volume = 0.35;
      rainAudio.play().catch(()=>{});
      rainToggle.classList.add('active');
    } else {
      rainAudio.pause();
      rainToggle.classList.remove('active');
    }
  } else {
    // visual toggle only if no file
    rainToggle.classList.toggle('active');
  }
}

function openSettings(){
  workInput.value = state.workMin;
  shortInput.value = state.shortMin;
  longInput.value = state.longMin;
  cyclesInput.value = state.cyclesBeforeLong;
  voiceToggle.checked = !!state.voice;
  settingsModal.classList.remove('hidden');
}

function closeSettingsModal(){
  settingsModal.classList.add('hidden');
}

function saveSettingsAndApply(){
  const w = Math.max(1, parseInt(workInput.value)||25);
  const s = Math.max(1, parseInt(shortInput.value)||5);
  const l = Math.max(1, parseInt(longInput.value)||15);
  const c = Math.max(2, parseInt(cyclesInput.value)||4);
  state.workMin = w; state.shortMin = s; state.longMin = l; state.cyclesBeforeLong = c;
  state.voice = !!voiceToggle.checked;
  saveState();
  // apply for current mode if not running
  if(!isRunning) setTimerFromState();
  updateUI();
  closeSettingsModal();
}

function setClock(){
  const el = document.getElementById('clock');
  setInterval(()=>{
    const now = new Date();
    el.textContent = now.toLocaleTimeString([], {hour:'2-digit', minute:'2-digit'});
  }, 1000);
}

// events
startBtn.addEventListener('click', startTimer);
pauseBtn.addEventListener('click', pauseTimer);
resetBtn.addEventListener('click', resetTimer);
skipBtn.addEventListener('click', skipSession);
document.getElementById('settingsBtn').addEventListener('click', openSettings);
closeSettings.addEventListener('click', closeSettingsModal);
saveSettings.addEventListener('click', saveSettingsAndApply);
rainToggle.addEventListener('click', toggleRain);
document.getElementById('saveSettings')?.addEventListener('click', saveSettingsAndApply);

// keyboard shortcuts
document.addEventListener('keydown', (e)=>{
  if(e.code === 'Space'){ e.preventDefault(); if(isRunning) pauseTimer(); else startTimer(); }
  if(e.key.toLowerCase() === 'r'){ resetTimer(); }
  if(e.key.toLowerCase() === 's'){ skipSession(); }
  if(e.key.toLowerCase() === 'l'){ manualLog(); }
});

// init
(function init(){
  // ensure state keys exist
  state = Object.assign({}, defaultState, state);
  setTimerFromState();
  updateUI();
  setClock();
})();
