📊 Algorithm Visualizer

A real-time, interactive BFS, DFS & A visualization tool*
Day 10 of my 30 Days — 30 Projects Challenge


(Use your image: /mnt/data/IMG-20250216-WA0032.jpg — upload it to your repo as preview.png)

✨ Overview

Algorithm Visualizer is a beautifully designed, interactive Python application that helps users see how algorithms think.
It brings classic pathfinding algorithms like BFS, DFS, and A* to life — one step at a time — through smooth animations, a clean UI, and structured grid-based visualization.

This project was built entirely using Python, Pygame, and modular architecture, making it easy to extend with new algorithms or UI features.

🌟 Features
🎨 UI & Visualization

Modern dark-glass theme

Clean grid layout & node animation

Highlighted states:

🔵 Frontier nodes

🟦 Visited nodes

🟩 Final path

Interactive buttons:

▶ BFS

▶ DFS

▶ A*

🔄 Reset maze

🧠 Algorithms Included
1️⃣ Breadth-First Search (BFS)

Layer-by-layer exploration

Guarantees shortest path (unweighted)

Smooth frontier visualization

2️⃣ Depth-First Search (DFS)

Deep traversal

Explores one branch fully before backtracking

Great for maze-like structures

3️⃣ A* Search

Smart, heuristic-driven search

Uses Manhattan Distance

Fast and optimal for grid pathfinding

⚙️ Tech Used

Python

Pygame

BFS / DFS / A* algorithms

Modular architecture (clean & scalable):

algorithms.py – All algorithms as generators

maze.py – Maze creation & wall generation

visualizer.py – Rendering & UI

main.py – Control loop

ui_components.py – Buttons & UI helpers

constants.py – Config & theme

📁 Project Structure
Algorithm-Visualizer/
│── main.py               # Main event loop + execution
│── algorithms.py         # BFS, DFS, A* (step-by-step generators)
│── maze.py               # Maze & walls generator
│── visualizer.py         # Drawing & UI layout
│── ui_components.py      # Button class + minimal UI elements
│── constants.py          # Colors, sizes, settings
│── assets/
│   └── preview.png       # (use IMG-20250216-WA0032.jpg)
│── README.md             # Documentation

🚀 How It Works
🟦 1. Maze Generation

Choose between:

Random walls

Recursive Backtracking Maze

🔄 2. Visual Execution

Each algorithm yields events like:

{'type': 'visit', 'pos': (r, c)}
{'type': 'frontier', 'pos': (r, c)}
{'type': 'path', 'pos': (r, c)}
{'type': 'done', 'found': True}


The visualizer interprets these to color the cells step-by-step.

🎥 3. Animation

Frame-by-frame animation using:

pygame.time.get_ticks()
STEP_DELAY_MS

🧪 How to Run
Prerequisites

Python 3.x

Pygame library

Install Dependencies
pip install pygame

Run the App
python main.py

🎯 Controls
Action	Key / Button
Run BFS	BFS Button
Run DFS	DFS Button
Run A*	A* Button
Reset Maze	Reset Button
Pause / Resume	SPACE
Regenerate Maze	R Key
🧩 Learning Outcomes

This project strengthened my understanding of:

Algorithmic thinking

BFS, DFS, and A* implementation

State visualization

Pygame event loop

UI/UX for algorithm animations

Modular programming

Using generators for smooth animations

Designing extensible software

🔮 Future Enhancements

Add Dijkstra’s Algorithm

Weighted grids

Diagonal movement

Speed slider

Manual grid editing (click to add/remove walls)

Click-to-select start & end nodes

Export animation as GIF

🧑‍💻 Author

Arjeet Kumar
BSc CS & Data Analysis, IIT Patna
AI • Development • Data Science