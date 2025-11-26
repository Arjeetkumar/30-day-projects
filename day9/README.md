# 🧩 Sudoku Solver App

A clean, interactive Sudoku game with a smart backtracking solver, auto puzzle generator, hints, error detection, and a modern Tkinter UI. Built as Day 9 of the 30 Days 30 Projects challenge.

## Sudoku Preview
<img width="1229" height="969" alt="Screenshot 2025-11-26 162151" src="https://github.com/user-attachments/assets/9f1668cf-2165-4395-8d85-e5c1c10068b0" />


### ✨ Features
## 🎨 Design

- Minimal, clean, and modern Tkinter interface

- Highlighted active cell

- Colored conflict detection

- Smooth grid rendering

- Responsive keyboard interaction

- Auto-generated Sudoku boards

## 🔢 Functionality

- Fully playable Sudoku board

- Auto-generate new puzzles with adjustable clues

- Backtracking-based auto-solver

- Hint system (fills one correct cell)

- Check Board feature

- Delete/Backspace support

- Smart input validation (1–9 only)

- Highlights invalid entries

- Never overwrites original puzzle clues

## ⌨️ Keyboard Support

- Numbers (1–9): Fill selected cell

- Arrow Keys: Navigate board

- Backspace/Delete: Clear selected cell

- Enter: Optional "Check Board"

- Mouse click: Select cell

## 📱 Implementation

- A lightweight Tkinter-only app — no external libraries needed.
Perfect for learning, experimenting, and extending.

### git clone https://github.com/Arjeetkumar/30-day-projects/edit/main/day9

## 📂 Project Structure
day9/
├── sudoku.py       # Main Tkinter UI + logic
├── README.md       # Documentation
└── assets/         # (Optional) screenshots

## 🎨 Styling Details

- Bold highlight for active cell

- Soft background color

- Red conflict colors

- Blue original clues

- Dynamic cell border glow on focus

## 🛠️ Technologies Used

- Python

- Tkinter

- Backtracking Algorithms

- Randomized Puzzle Generation

## 🔮 Future Enhancements

- Pencil marks (notes mode)

- Undo / Redo

- Difficulty rating (Easy/Medium/Hard)

- Step-by-step solving animation

- Daily challenges

- Save/Load puzzles

## 🐛 Known Issues

- Unique puzzle generation can be slow on extremely low clue settings

- Visualization is instant (no solver animation yet)

## 📝 Learning Outcomes

This project helped me practice:

- Backtracking algorithms

- Grid-based UI design

- Event-driven programming in Tkinter

- State management in Python

- Puzzle generation logic

- Clean code structure

- Error highlighting & validation

## 👨‍💻 Author

### Arjeet Kumar

Day 9 — 30 Days 30 Projects Challenge
