🧮 Day 1 — Neo Glassmorphism Calculator

A futuristic, glass-effect calculator with glowing buttons, smooth animations, advanced keyboard support, and clean JavaScript logic.
Built as Day 1 of the 30 Days 30 Projects Challenge.

✨ Features
🎨 Modern UI (Unique Design)

Glassmorphism style with blur effects

Soft neon-glow buttons

Gradient background

Floating rounded keys

Animated header

🔢 Calculator Functionality

Addition, subtraction, multiplication, division

Decimal point support

Negative number toggle (+/-)

Backspace/delete

Prevents invalid decimal inputs

Prevents division by zero

Smooth, continuous calculations

⌨️ Keyboard Support

Numbers (0–9)

Operators (+, –, *, /)

Enter → Equals

Backspace → Delete last digit

Escape → Clear all

“.” → Decimal

“n” → Toggle negative number

📱 Responsive

Dynamic layout for mobile screens

Auto-resizing display text

Touch-friendly buttons

📸 UI Preview

(Add screenshot here if needed)

🛠️ Tech Stack

HTML5 – Markup

CSS3 – Glassmorphism + Grid/Flexbox

JavaScript (Vanilla) – Calculator logic + keyboard events

📂 Project Structure
day1/
├── index.html          # UI Structure
├── style.css           # Glassmorphism Styling
├── script.js           # Calculator Logic
└── README.md           # Documentation

🚀 Getting Started
📦 Clone the Repository
git clone https://github.com/YOUR-USERNAME/30-days-30-projects.git
cd day1

▶️ Run the Web Version
Option 1 – Simply open:
index.html

Option 2 – Run a local server:
python -m http.server 8000


Then open:

http://localhost:8000

🎯 How to Use
Web Calculator

Click numbers to input

Select operator: +, –, ×, ÷

Press "=" or Enter to get result

Use “C” to clear all

Use "⌫" to delete last digit

Press “+/-” to toggle negative number

Keyboard Shortcuts
Key	Action
0–9	Enter numbers
+ - * /	Operators
Enter	Equals
Escape	Clear
Backspace	Delete
.	Decimal
n	Negative toggle
💡 Code Highlights
✔ Prevent Double Decimal
if (num === "." && current.includes(".")) return;

✔ Negative Number Toggle
current = current.startsWith("-") ? current.slice(1) : "-" + current;

✔ Division by Zero Protection
if (op === "/" && b === 0) {
    alert("Cannot divide by zero");
    clearAll();
}

🔮 Future Enhancements

History panel

Dark/Light themes

Scientific mode

Sound effects

Button animations on press

LocalStorage memory

📚 Learning Outcomes

This project helped practice:

Event-driven JavaScript

State management

UI/UX design

Keyboard event handling

Grid-based layouting

Glassmorphism design

Clean function-based logic

👨‍💻 Author

Arjeet Kumar
30 Days 30 Projects Challenge