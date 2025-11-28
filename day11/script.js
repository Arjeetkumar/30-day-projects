/* Habit Quest - Cyberpunk Edition Logic */

const STORAGE_KEY = 'habit_quest_v2';

// --- Sound Manager ---
class SoundManager {
  constructor() {
    this.ctx = new (window.AudioContext || window.webkitAudioContext)();
    this.enabled = true;
  }

  playTone(freq, type, duration, vol = 0.1) {
    if (!this.enabled) return;
    const osc = this.ctx.createOscillator();
    const gain = this.ctx.createGain();
    osc.type = type;
    osc.frequency.setValueAtTime(freq, this.ctx.currentTime);
    gain.gain.setValueAtTime(vol, this.ctx.currentTime);
    gain.gain.exponentialRampToValueAtTime(0.01, this.ctx.currentTime + duration);
    osc.connect(gain);
    gain.connect(this.ctx.destination);
    osc.start();
    osc.stop(this.ctx.currentTime + duration);
  }

  playTick() { this.playTone(800, 'sine', 0.1, 0.1); }
  playComplete() {
    this.playTone(400, 'triangle', 0.1, 0.1);
    setTimeout(() => this.playTone(600, 'triangle', 0.2, 0.1), 100);
    setTimeout(() => this.playTone(1000, 'triangle', 0.4, 0.1), 200);
  }
  playLevelUp() {
    [200, 300, 400, 500, 800].forEach((f, i) => setTimeout(() => this.playTone(f, 'square', 0.2, 0.05), i * 80));
  }
}

const audio = new SoundManager();

// --- State & Data ---
let habits = [];
let profile = { points: 0, level: 1, history: {} }; // history: { "YYYY-MM-DD": points_earned }
let editingId = null;

const today = () => new Date().toISOString().slice(0, 10);
const uid = () => Math.random().toString(36).slice(2) + Date.now().toString(36);

// --- DOM Elements ---
const els = {
  grid: document.getElementById('grid'),
  points: document.getElementById('pointsValue'),
  level: document.getElementById('levelText'),
  nextLevel: document.getElementById('nextLevelText'),
  levelFill: document.getElementById('levelFill'),
  chart: document.getElementById('weeklyChart'),
  modal: document.getElementById('modal'),
  modalTitle: document.getElementById('modalTitle'),
  inputs: {
    name: document.getElementById('name'),
    goal: document.getElementById('goal'),
    color: document.getElementById('color'),
    pts: document.getElementById('pts'),
    bonus: document.getElementById('bonus')
  },
  floatRoot: document.getElementById('floatRoot')
};

// --- Initialization ---
function init() {
  loadData();
  // Seed if empty
  if (habits.length === 0) {
    habits.push({
      id: uid(),
      name: "Drink Water",
      goal: 5,
      color: "#00f2ff",
      pts: 10,
      bonus: 50,
      history: {},
      created: Date.now()
    });
    saveData();
  }
  render();
  renderProfile();
  renderChart();

  // Unlock audio context on first interaction
  document.body.addEventListener('click', () => {
    if (audio.ctx.state === 'suspended') audio.ctx.resume();
  }, { once: true });
}

// --- Core Logic ---

function loadData() {
  try {
    const raw = localStorage.getItem(STORAGE_KEY);
    if (raw) {
      const data = JSON.parse(raw);
      habits = data.habits || [];
      profile = { ...profile, ...data.profile };
    }
  } catch (e) { console.error("Load failed", e); }
}

function saveData() {
  localStorage.setItem(STORAGE_KEY, JSON.stringify({ habits, profile }));
  renderProfile();
  renderChart();
}

function getStreak(habit) {
  let streak = 0;
  const d = new Date();
  // Check yesterday, then day before...
  // If today is done, streak includes today? Usually streak is consecutive *past* days + today if done.
  // Let's count consecutive days ending yesterday or today.

  // Simple algo: check backwards from today
  let checkDate = new Date();
  while (true) {
    const dateStr = checkDate.toISOString().slice(0, 10);
    const count = habit.history[dateStr] || 0;

    // If it's today and not done, don't break streak yet
    if (dateStr === today() && count < habit.goal) {
      checkDate.setDate(checkDate.getDate() - 1);
      continue;
    }

    if (count >= habit.goal) {
      streak++;
      checkDate.setDate(checkDate.getDate() - 1);
    } else {
      break;
    }
  }
  return streak;
}

function gain(id) {
  const h = habits.find(x => x.id === id);
  if (!h) return;

  const d = today();
  h.history = h.history || {};
  const current = h.history[d] || 0;

  h.history[d] = current + 1;

  // Points logic
  const pts = parseInt(h.pts) || 10;
  addPoints(pts);
  showFloat(`+${pts}`, event.clientX, event.clientY, h.color);

  // Bonus check
  if (h.history[d] === parseInt(h.goal)) {
    const bonus = parseInt(h.bonus) || 50;
    addPoints(bonus);
    showFloat(`BONUS +${bonus}!`, window.innerWidth / 2, window.innerHeight / 2, '#ffd700', true);
    audio.playComplete();
  } else {
    audio.playTick();
  }

  saveData();
  render();
}

function undo(id) {
  const h = habits.find(x => x.id === id);
  if (!h) return;
  const d = today();
  if (!h.history[d]) return;

  h.history[d]--;
  if (h.history[d] <= 0) delete h.history[d];

  // Deduct points (simplified, doesn't remove bonus explicitly to avoid complexity)
  profile.points = Math.max(0, profile.points - (parseInt(h.pts) || 10));

  saveData();
  render();
}

function addPoints(amount) {
  profile.points += amount;

  // Track history for chart
  const d = today();
  profile.history = profile.history || {};
  profile.history[d] = (profile.history[d] || 0) + amount;

  // Level check
  const oldLevel = profile.level;
  const newLevel = Math.floor(profile.points / 500) + 1;
  if (newLevel > oldLevel) {
    profile.level = newLevel;
    showFloat(`LEVEL UP! ${newLevel}`, window.innerWidth / 2, window.innerHeight / 3, '#bd00ff', true);
    audio.playLevelUp();
  }
}

// --- Rendering ---

function render() {
  els.grid.innerHTML = '';
  const q = document.getElementById('search').value.toLowerCase();

  habits.forEach(h => {
    if (q && !h.name.toLowerCase().includes(q)) return;

    const d = today();
    const count = h.history[d] || 0;
    const goal = parseInt(h.goal) || 1;
    const pct = Math.min(100, Math.round((count / goal) * 100));
    const streak = getStreak(h);

    // SVG Ring calculation
    const radius = 16; // r=16 -> circumference ~100
    const dashArray = 100;
    const dashOffset = 100 - (pct); // 0 to 100

    const el = document.createElement('article');
    el.className = 'card';
    el.style.setProperty('--card-color', h.color);
    el.innerHTML = `
            <div class="card-head">
                <div>
                    <div class="card-title">${h.name}</div>
                    <div class="card-meta">Goal: ${goal} • ${h.pts} pts</div>
                </div>
                ${streak > 1 ? `<div class="streak-badge">🔥 ${streak}</div>` : ''}
            </div>
            
            <div class="progress-container">
                <div class="ring-wrapper">
                    <svg class="ring-svg" viewBox="0 0 40 40">
                        <circle class="ring-circle-bg" cx="20" cy="20" r="${radius}"></circle>
                        <circle class="ring-circle-fg" cx="20" cy="20" r="${radius}" 
                                style="stroke-dashoffset: ${dashOffset};"></circle>
                    </svg>
                    <div class="ring-text">${count}</div>
                </div>
                <div class="progress-stats">
                    <div class="stat-row">
                        <span class="stat-label">Progress</span>
                        <span class="stat-val">${pct}%</span>
                    </div>
                    <div class="level-bar"><div class="level-fill" style="width:${pct}%; background:${h.color}"></div></div>
                </div>
            </div>
            
            <div class="card-actions">
                <button class="action-btn" onclick="undo('${h.id}')">−</button>
                <button class="action-btn primary" onclick="gain('${h.id}')">+</button>
                <button class="action-btn" onclick="editHabit('${h.id}')">✎</button>
            </div>
        `;
    els.grid.appendChild(el);
  });
}

function renderProfile() {
  els.points.textContent = profile.points.toLocaleString();
  els.level.textContent = `Level ${profile.level}`;

  const nextLvlPts = profile.level * 500;
  const prevLvlPts = (profile.level - 1) * 500;
  const progress = profile.points - prevLvlPts;
  const needed = 500;
  const pct = Math.min(100, (progress / needed) * 100);

  els.nextLevel.textContent = `${500 - progress} XP to next`;
  els.levelFill.style.width = `${pct}%`;
}

function renderChart() {
  els.chart.innerHTML = '';
  const days = [];
  for (let i = 6; i >= 0; i--) {
    const d = new Date();
    d.setDate(d.getDate() - i);
    days.push(d.toISOString().slice(0, 10));
  }

  const maxVal = Math.max(...days.map(d => profile.history[d] || 0), 100);

  days.forEach(d => {
    const val = profile.history[d] || 0;
    const h = Math.max(4, (val / maxVal) * 100);
    const bar = document.createElement('div');
    bar.className = 'bar';
    bar.style.height = `${h}%`;
    bar.innerHTML = `<div class="bar-tooltip">${val} pts<br>${d.slice(5)}</div>`;
    els.chart.appendChild(bar);
  });
}

// --- Floating Text ---
function showFloat(text, x, y, color, big = false) {
  const el = document.createElement('div');
  el.className = 'float-text';
  el.textContent = text;
  el.style.left = x + 'px';
  el.style.top = y + 'px';
  el.style.color = color || '#fff';
  if (big) el.style.fontSize = '32px';
  els.floatRoot.appendChild(el);
  setTimeout(() => el.remove(), 1000);
}

// --- Modal & Form ---
window.editHabit = function (id) {
  editingId = id;
  const h = habits.find(x => x.id === id);
  if (h) {
    els.modalTitle.textContent = 'Edit Habit';
    els.inputs.name.value = h.name;
    els.inputs.goal.value = h.goal;
    els.inputs.color.value = h.color;
    els.inputs.pts.value = h.pts;
    els.inputs.bonus.value = h.bonus;
    document.getElementById('deleteBtn').style.display = 'block';
  }
  els.modal.classList.add('active');
};

document.getElementById('newBtn').onclick = () => {
  editingId = null;
  els.modalTitle.textContent = 'New Habit';
  els.inputs.name.value = '';
  els.inputs.goal.value = 1;
  els.inputs.color.value = '#00f2ff';
  els.inputs.pts.value = 10;
  els.inputs.bonus.value = 50;
  document.getElementById('deleteBtn').style.display = 'none';
  els.modal.classList.add('active');
};

document.getElementById('cancelBtn').onclick = () => els.modal.classList.remove('active');

document.getElementById('saveBtn').onclick = () => {
  const name = els.inputs.name.value.trim();
  if (!name) return alert('Name required');

  const data = {
    name,
    goal: parseInt(els.inputs.goal.value) || 1,
    color: els.inputs.color.value,
    pts: parseInt(els.inputs.pts.value) || 10,
    bonus: parseInt(els.inputs.bonus.value) || 50,
    updated: Date.now()
  };

  if (editingId) {
    const h = habits.find(x => x.id === editingId);
    Object.assign(h, data);
  } else {
    habits.push({ id: uid(), ...data, history: {}, created: Date.now() });
  }

  saveData();
  els.modal.classList.remove('active');
  render();
};

document.getElementById('deleteBtn').onclick = () => {
  if (!editingId || !confirm('Delete this habit?')) return;
  habits = habits.filter(h => h.id !== editingId);
  saveData();
  els.modal.classList.remove('active');
  render();
};

document.getElementById('search').oninput = render;

// --- Export/Import ---
document.getElementById('exportBtn').onclick = () => {
  const blob = new Blob([JSON.stringify({ habits, profile }, null, 2)], { type: 'application/json' });
  const url = URL.createObjectURL(blob);
  const a = document.createElement('a');
  a.href = url;
  a.download = `habit-quest-${today()}.json`;
  document.body.appendChild(a);
  a.click();
  a.remove();
};

document.getElementById('importBtn').onclick = () => document.getElementById('fileInput').click();
document.getElementById('fileInput').onchange = (e) => {
  const f = e.target.files[0];
  if (!f) return;
  const r = new FileReader();
  r.onload = (ev) => {
    try {
      const d = JSON.parse(ev.target.result);
      if (d.habits) {
        habits = d.habits;
        profile = d.profile || profile;
        saveData();
        render();
        alert('Import successful!');
      }
    } catch (err) { alert('Invalid file'); }
  };
  r.readAsText(f);
};

// Start
init();
