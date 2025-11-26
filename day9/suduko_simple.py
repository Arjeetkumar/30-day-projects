"""
Simple Sudoku - single-file Tkinter app
Features:
- Generate full solution (backtracking)
- Make puzzle by removing cells
- Simple uniqueness-check during removal (limits attempts)
- Playable UI: click cell and type 1-9
- Hint, Solve, New Puzzle, Clear, Check buttons
"""

import tkinter as tk
from tkinter import messagebox, simpledialog
import random
from copy import deepcopy
import time

# ---------------------------
# Sudoku logic (solver/generator)
# ---------------------------
def find_empty(grid):
    for r in range(9):
        for c in range(9):
            if grid[r][c] == 0:
                return r, c
    return None

def is_valid(grid, r, c, v):
    # row/col
    for i in range(9):
        if grid[r][i] == v or grid[i][c] == v:
            return False
    # 3x3 block
    br, bc = (r//3)*3, (c//3)*3
    for i in range(br, br+3):
        for j in range(bc, bc+3):
            if grid[i][j] == v:
                return False
    return True

def solve_backtracking(grid):
    empty = find_empty(grid)
    if not empty:
        return True
    r, c = empty
    for v in range(1, 10):
        if is_valid(grid, r, c, v):
            grid[r][c] = v
            if solve_backtracking(grid):
                return True
            grid[r][c] = 0
    return False

def count_solutions(grid, limit=2):
    # count solutions up to 'limit' (used to try to preserve uniqueness)
    grid = deepcopy(grid)
    count = 0
    def backtrack():
        nonlocal count
        if count >= limit:
            return
        e = find_empty(grid)
        if not e:
            count += 1
            return
        r,c = e
        for v in range(1,10):
            if is_valid(grid, r, c, v):
                grid[r][c] = v
                backtrack()
                grid[r][c] = 0
                if count >= limit:
                    return
    backtrack()
    return count

def generate_full_solution(seed=None):
    if seed is not None:
        random.seed(seed)
    grid = [[0]*9 for _ in range(9)]
    nums = list(range(1,10))
    def fill():
        e = find_empty(grid)
        if not e:
            return True
        r,c = e
        random.shuffle(nums)
        for v in nums:
            if is_valid(grid, r, c, v):
                grid[r][c] = v
                if fill():
                    return True
                grid[r][c] = 0
        return False
    fill()
    return grid

def make_puzzle(full_grid, clues=30, ensure_unique=True):
    # clones full_grid and removes cells until only 'clues' remain
    grid = deepcopy(full_grid)
    cells = [(r,c) for r in range(9) for c in range(9)]
    random.shuffle(cells)
    removals = 81 - clues
    attempts = 0
    removed = 0
    for (r,c) in cells:
        if removed >= removals:
            break
        attempts += 1
        backup = grid[r][c]
        grid[r][c] = 0
        if ensure_unique:
            # quick uniqueness check; expensive if many removals -> we limit attempts
            sol_count = count_solutions(grid, limit=2)
            if sol_count != 1:
                grid[r][c] = backup  # revert
            else:
                removed += 1
        else:
            removed += 1
    return grid

# ---------------------------
# Simple GUI
# ---------------------------
class SimpleSudokuApp:
    def __init__(self, master):
        self.master = master
        master.title("Simple Sudoku — Arjeet")
        
        # Increased cell size for larger screen area
        self.cell_size = 65
        w = self.cell_size*9 + 40
        h = self.cell_size*9 + 160
        master.geometry(f"{w}x{h}")
        master.resizable(False, False)

        # Headline
        tk.Label(master, text="Simple Sudoku", font=("Helvetica", 24, "bold"), fg="#333").pack(pady=(10, 0))

        self.full = generate_full_solution()
        self.puzzle = make_puzzle(self.full, clues=36, ensure_unique=True)
        self.grid = deepcopy(self.puzzle)  # player grid

        self.selected = (0,0)

        # canvas for board
        self.canvas = tk.Canvas(master, width=self.cell_size*9+4, height=self.cell_size*9+4, bg="#f6f6f6")
        self.canvas.pack(padx=20, pady=20)
        self.canvas.bind("<Button-1>", self.click_cell)
        master.bind("<Key>", self.on_key)

        # control buttons
        frame = tk.Frame(master)
        frame.pack(pady=6)
        tk.Button(frame, text="New Puzzle", command=self.new_puzzle).grid(row=0, column=0, padx=4)
        tk.Button(frame, text="Solve", command=self.solve).grid(row=0, column=1, padx=4)
        tk.Button(frame, text="Hint", command=self.hint).grid(row=0, column=2, padx=4)
        tk.Button(frame, text="Check", command=self.check).grid(row=0, column=3, padx=4)
        tk.Button(frame, text="Clear", command=self.clear_entries).grid(row=0, column=4, padx=4)
        tk.Button(frame, text="Full Screen", command=self.toggle_fullscreen).grid(row=0, column=5, padx=4)

        # Fullscreen bindings
        master.bind("<F11>", self.toggle_fullscreen)
        master.bind("<Escape>", self.exit_fullscreen)
        self.is_fullscreen = False

        # slider for clues
        sframe = tk.Frame(master)
        sframe.pack()
        tk.Label(sframe, text="Clues:").pack(side="left")
        self.clues_var = tk.IntVar(value=36)
        clues_scale = tk.Scale(sframe, from_=22, to=60, orient="horizontal", variable=self.clues_var)
        clues_scale.pack(side="left")

        self.draw_board()

    def draw_board(self):
        self.canvas.delete("all")
        cs = self.cell_size
        # cells
        for r in range(9):
            for c in range(9):
                x = 2 + c*cs
                y = 2 + r*cs
                is_selected = (r,c) == self.selected
                fill = "#fff" if (r+c)%2==0 else "#fafafa"
                if is_selected: fill = "#e4f0ff"
                self.canvas.create_rectangle(x,y,x+cs,y+cs, fill=fill, outline="#444")
                val = self.grid[r][c]
                if val != 0:
                    color = "#000" if self.puzzle[r][c]==0 else "#1f3a93"  # blue for given
                    self.canvas.create_text(x+cs/2, y+cs/2, text=str(val), font=("Arial", 16, "bold"), fill=color)
        # thick lines
        for i in range(10):
            lw = 3 if i%3==0 else 1
            pos = 2 + i*cs
            self.canvas.create_line(2, pos, 2+9*cs, pos, width=lw, fill="#333")
            self.canvas.create_line(pos, 2, pos, 2+9*cs, width=lw, fill="#333")

    def click_cell(self, event):
        cs = self.cell_size
        c = int((event.x-2) // cs)
        r = int((event.y-2) // cs)
        if 0 <= r < 9 and 0 <= c < 9:
            self.selected = (r,c)
            self.draw_board()

    def on_key(self, event):
        k = event.char
        if k in "123456789":
            r,c = self.selected
            if self.puzzle[r][c] == 0:  # editable
                self.grid[r][c] = int(k)
                self.draw_board()
        elif event.keysym in ("BackSpace", "Delete"):
            r,c = self.selected
            if self.puzzle[r][c] == 0:
                self.grid[r][c] = 0
                self.draw_board()
        elif event.keysym == "Left":
            r,c = self.selected; self.selected = (r, max(0,c-1)); self.draw_board()
        elif event.keysym == "Right":
            r,c = self.selected; self.selected = (r, min(8,c+1)); self.draw_board()
        elif event.keysym == "Up":
            r,c = self.selected; self.selected = (max(0,r-1), c); self.draw_board()
        elif event.keysym == "Down":
            r,c = self.selected; self.selected = (min(8,r+1), c); self.draw_board()
        elif event.char.lower() == "n":
            self.new_puzzle()

    def new_puzzle(self):
        clues = self.clues_var.get()
        self.full = generate_full_solution()
        # try uniqueness but limit attempts for speed
        self.puzzle = make_puzzle(self.full, clues=clues, ensure_unique=True)
        self.grid = deepcopy(self.puzzle)
        self.selected = (0,0)
        self.draw_board()

    def solve(self):
        grid_copy = deepcopy(self.grid)
        if solve_backtracking(grid_copy):
            self.grid = grid_copy
            self.draw_board()
            messagebox.showinfo("Solved", "Solution applied to board.")
        else:
            messagebox.showwarning("No solution", "Current board has no valid solution.")

    def hint(self):
        # place a correct value at a random empty cell if possible
        empties = [(r,c) for r in range(9) for c in range(9) if self.grid[r][c]==0]
        if not empties:
            messagebox.showinfo("Hint", "No empty cells.")
            return
        # prefer cells with single candidate
        for r,c in empties:
            candidates = [v for v in range(1,10) if is_valid(self.grid, r, c, v)]
            if len(candidates) == 1:
                self.grid[r][c] = candidates[0]
                self.draw_board()
                return
        # otherwise place correct value from full solution
        r,c = random.choice(empties)
        self.grid[r][c] = self.full[r][c]
        self.draw_board()

    def check(self):
        # check if any cell violates rules
        for r in range(9):
            for c in range(9):
                v = self.grid[r][c]
                if v == 0: continue
                # temporarily clear and test
                self.grid[r][c] = 0
                if not is_valid(self.grid, r, c, v):
                    self.grid[r][c] = v
                    messagebox.showwarning("Check", f"Conflict at row {r+1}, col {c+1} with value {v}.")
                    return
                self.grid[r][c] = v
        # if no conflicts, check completeness
        if all(self.grid[r][c] != 0 for r in range(9) for c in range(9)):
            messagebox.showinfo("Check", "Board is valid and complete. Well done!")
        else:
            messagebox.showinfo("Check", "No conflicts found so far.")

    def toggle_fullscreen(self, event=None):
        self.is_fullscreen = not self.is_fullscreen
        self.master.attributes("-fullscreen", self.is_fullscreen)
        if not self.is_fullscreen:
            self.master.geometry(f"{self.cell_size*9+40}x{self.cell_size*9+160}")

    def exit_fullscreen(self, event=None):
        self.is_fullscreen = False
        self.master.attributes("-fullscreen", False)
        self.master.geometry(f"{self.cell_size*9+40}x{self.cell_size*9+160}")

    def clear_entries(self):
        for r in range(9):
            for c in range(9):
                if self.puzzle[r][c] == 0:
                    self.grid[r][c] = 0
        self.draw_board()

if __name__ == "__main__":
    root = tk.Tk()
    app = SimpleSudokuApp(root)
    root.mainloop()
