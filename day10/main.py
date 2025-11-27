# main.py
import pygame, sys, time
from constants import *
from maze import generate_random_walls, recursive_backtracker_maze
from visualizer import Visualizer
from algorithms import bfs, dfs, a_star

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Algo_Visualizer - Arjeet")
clock = pygame.time.Clock()

# choose grid
ROWS = GRID_ROWS
COLS = GRID_COLS
# grid = generate_random_walls(ROWS, COLS, density=0.28, seed=42)
grid = recursive_backtracker_maze(ROWS, COLS, seed=42)

# start and goal (avoid walls)
def find_non_wall(grid, prefer=(0,0)):
    R = len(grid)
    C = len(grid[0])
    pr,pc = prefer
    if 0 <= pr < R and 0 <= pc < C and grid[pr][pc]==0:
        return pr,pc
    for r in range(R):
        for c in range(C):
            if grid[r][c]==0:
                return r,c
    return 0,0

start = find_non_wall(grid, (1,1))
goal = find_non_wall(grid, (ROWS-2, COLS-2))

viz = Visualizer(screen, grid, start, goal)

alg_gen = None
last_step_time = 0
running = True
paused = False

def start_algorithm(name):
    global alg_gen, last_step_time, paused
    viz.reset_visuals()
    if name == 'BFS':
        alg_gen = bfs(grid, start, goal)
    elif name == 'DFS':
        alg_gen = dfs(grid, start, goal)
    elif name == 'A*':
        alg_gen = a_star(grid, start, goal)
    else:
        alg_gen = None
    viz.info_text = f"Running {name}..."
    last_step_time = pygame.time.get_ticks()
    paused = False

def reset_all():
    global grid, viz, alg_gen
    grid = recursive_backtracker_maze(ROWS, COLS, seed=None)
    viz = Visualizer(screen, grid, find_non_wall(grid,(1,1)), find_non_wall(grid,(ROWS-2,COLS-2)))
    alg_gen = None

while running:
    dt = clock.tick(FPS)
    now = pygame.time.get_ticks()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mx,my = event.pos
            if viz.btn_bfs.clicked((mx,my)):
                start_algorithm('BFS')
            elif viz.btn_dfs.clicked((mx,my)):
                start_algorithm('DFS')
            elif viz.btn_astar.clicked((mx,my)):
                start_algorithm('A*')
            elif viz.btn_reset.clicked((mx,my)):
                reset_all()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                paused = not paused
                viz.info_text = "Paused" if paused else "Running..."
            elif event.key == pygame.K_r:
                reset_all()

    # advance algorithm generator at STEP_DELAY_MS
    if alg_gen and not paused and (now - last_step_time) >= STEP_DELAY_MS:
        last_step_time = now
        try:
            step = next(alg_gen)
            stype = step.get('type')
            pos = step.get('pos')
            if stype == 'visit' and pos:
                viz.visited.add(pos)
                if pos in viz.frontier:
                    viz.frontier.discard(pos)
            elif stype == 'frontier' and pos:
                viz.frontier.add(pos)
            elif stype == 'path' and pos:
                viz.path.append(pos)
            elif stype == 'done':
                if step.get('found'):
                    viz.info_text = "Path found ✅"
                else:
                    viz.info_text = "No path found ❌"
                alg_gen = None
        except StopIteration:
            alg_gen = None

    # draw
    viz.draw()
    pygame.display.flip()

pygame.quit()
sys.exit()
