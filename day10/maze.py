# maze.py
import random

def empty_grid(rows, cols, default=0):
    return [[default for _ in range(cols)] for __ in range(rows)]

def generate_random_walls(rows, cols, density=0.25, seed=None):
    """
    Randomly scatter walls across the grid.
    density: fraction of cells that are walls
    """
    if seed is not None:
        random.seed(seed)
    grid = empty_grid(rows, cols, 0)
    for r in range(rows):
        for c in range(cols):
            if random.random() < density:
                grid[r][c] = 1
    return grid

def recursive_backtracker_maze(rows, cols, seed=None):
    """
    Simple maze generation using recursive backtracker on a grid of 'cells'
    We will create a grid that uses odd indices as corridors to allow walls.
    Produces grid with walls (1) and open (0).
    """
    if seed is not None:
        random.seed(seed)
    # Build a (2*rows+1) x (2*cols+1) grid if needed.
    out_rows = rows
    out_cols = cols

    grid = [[1 for _ in range(out_cols)] for __ in range(out_rows)]

    # treat each cell as node if both row and col are odd (or just use a simpler approach)
    # We'll do a simpler randomized DFS carve:
    dirs = [(0,1),(1,0),(0,-1),(-1,0)]

    def in_bounds(r,c):
        return 0 <= r < out_rows and 0 <= c < out_cols

    # start from a random cell
    start = (random.randrange(1, out_rows, 2) if out_rows%2==1 else random.randrange(0,out_rows),
             random.randrange(1, out_cols, 2) if out_cols%2==1 else random.randrange(0,out_cols))
    stack = [start]
    grid[start[0]][start[1]] = 0

    while stack:
        r,c = stack[-1]
        neighbors = []
        for dr,dc in dirs:
            nr, nc = r + dr*2, c + dc*2
            if in_bounds(nr, nc) and grid[nr][nc] == 1:
                neighbors.append((nr,nc,dr,dc))
        if neighbors:
            nr,nc,dr,dc = random.choice(neighbors)
            # carve mid cell
            midr, midc = r + dr, c + dc
            grid[midr][midc] = 0
            grid[nr][nc] = 0
            stack.append((nr,nc))
        else:
            stack.pop()
    return grid
