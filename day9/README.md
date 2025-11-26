🧩 Sudoku Solver App

A clean, interactive Sudoku game with a smart backtracking solver, auto puzzle generator, hints, error detection, and a modern Tkinter UI. Built as Day 9 of the 30 Days 30 Projects challenge.

Sudoku Preview
(Attach your screenshot here)

✨ Features
🎨 Design

Minimal, clean, and modern Tkinter interface

Highlighted active cell

Colored conflict detection

Smooth grid rendering

Responsive keyboard interaction

Auto-generated Sudoku boards

🔢 Functionality

Fully playable Sudoku board

Auto-generate new puzzles with adjustable clues

Backtracking-based auto-solver

Hint system (fills one correct cell)

Check Board feature

Delete/Backspace support

Smart input validation (1–9 only)

Highlights invalid entries

Never overwrites original puzzle clues

⌨️ Keyboard Support

Numbers (1–9): Fill selected cell

Arrow Keys: Navigate board

Backspace/Delete: Clear selected cell

Enter: Optional "Check Board"

Mouse click: Select cell

📱 Implementation

A lightweight Tkinter-only app — no external libraries needed.
Perfect for learning, experimenting, and extending.

🚀 Getting Started
Prerequisites

Python 3.7+

Tkinter (built into most Python installations)

Installation
git clone <your-repo-link-here>
cd sudoku-day9
python sudoku.py

📂 Project Structure
day9/
├── sudoku.py       # Main Tkinter UI + logic
├── README.md       # Documentation
└── assets/         # (Optional) screenshots

🎯 How to Use
Play Sudoku

Click a cell and type numbers 1–9

Invalid placements are highlighted red

Use arrow keys to move around

Generate Puzzle

Click New Puzzle

Adjust number of clues (difficulty slider)

Hints

Click Hint

One correct number appears in an empty cell

Auto Solve

Click Solve to instantly complete the board

Check the Board

Click Check

Highlights wrong placements or congratulates if solved

Clear

Clears only user-filled cells

💻 Code Highlights
✔️ Sudoku Generator (Backtracking)

Creates a valid full Sudoku grid, then removes cells based on difficulty.

✔️ Solver Algorithm

Classic DFS backtracking solver:

def solve(board):
    r, c = find_empty(board)
    if not (r, c):
        return True
    for num in '123456789':
        if valid(board, r, c, num):
            board[r][c] = num
            if solve(board):
                return True
            board[r][c] = '.'
    return False

✔️ UI Rendering

Canvas-based board with live redraw & highlight effects.

✔️ Hint Function

Injects one number from the solved grid into the playable board.

🎨 Styling Details

Bold highlight for active cell

Soft background color

Red conflict colors

Blue original clues

Dynamic cell border glow on focus

🛠️ Technologies Used

Python

Tkinter

Backtracking Algorithms

Randomized Puzzle Generation

🔮 Future Enhancements

Pencil marks (notes mode)

Undo / Redo

Difficulty rating (Easy/Medium/Hard)

Step-by-step solving animation

Daily challenges

Save/Load puzzles

🐛 Known Issues

Unique puzzle generation can be slow on extremely low clue settings

Visualization is instant (no solver animation yet)

📝 Learning Outcomes

This project helped me practice:

Backtracking algorithms

Grid-based UI design

Event-driven programming in Tkinter

State management in Python

Puzzle generation logic

Clean code structure

Error highlighting & validation

👨‍💻 Author

Arjeet Kumar
Day 9 — 30 Days 30 Projects Challenge