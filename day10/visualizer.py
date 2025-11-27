# visualizer.py
import pygame
import time
from constants import *
from ui_components import Button

class Visualizer:
    def __init__(self, screen, grid, start, goal):
        self.screen = screen
        self.grid = grid
        self.start = start
        self.goal = goal
        self.rows = len(grid)
        self.cols = len(grid[0])
        self.cell_w = CELL_SIZE
        self.cell_h = CELL_SIZE
        self.offset_x = MARGIN_X
        self.offset_y = MARGIN_Y
        self.visited = set()
        self.frontier = set()
        self.path = []
        self.info_text = "Press Generate (BFS/DFS/A*)"

        # Controls
        self.btn_bfs = Button((20,20,90,36), "BFS")
        self.btn_dfs = Button((120,20,90,36), "DFS")
        self.btn_astar = Button((220,20,90,36), "A*")
        self.btn_reset = Button((600,20,90,36), "Reset")
        self.buttons = [self.btn_bfs, self.btn_dfs, self.btn_astar, self.btn_reset]

    def reset_visuals(self):
        self.visited.clear()
        self.frontier.clear()
        self.path = []
        self.info_text = "Ready"

    def cell_to_rect(self, r, c):
        x = self.offset_x + c * self.cell_w
        y = self.offset_y + r * self.cell_h
        return pygame.Rect(x, y, self.cell_w-1, self.cell_h-1)

    def draw(self):
        surf = self.screen
        # background card
        pygame.draw.rect(surf, COLOR_CARD, (0, 0, WIDTH, HEIGHT))

        # draw buttons
        for btn in self.buttons:
            btn.draw(surf)

        # draw info
        font = pygame.font.SysFont("Arial", 16)
        info = font.render(self.info_text, True, COLOR_TEXT)
        surf.blit(info, (340, 28))

        # draw grid cells
        for r in range(self.rows):
            for c in range(self.cols):
                rect = self.cell_to_rect(r, c)
                if self.grid[r][c] == 1:
                    color = COLOR_WALL
                else:
                    color = COLOR_OPEN
                pygame.draw.rect(surf, color, rect)

        # visited
        for (r,c) in self.visited:
            rect = self.cell_to_rect(r,c)
            pygame.draw.rect(surf, COLOR_VISITED, rect)

        # frontier
        for (r,c) in self.frontier:
            rect = self.cell_to_rect(r,c)
            pygame.draw.rect(surf, COLOR_FRONTIER, rect)

        # path
        for (r,c) in self.path:
            rect = self.cell_to_rect(r,c)
            pygame.draw.rect(surf, COLOR_PATH, rect)

        # start & goal
        pygame.draw.rect(surf, COLOR_START, self.cell_to_rect(*self.start))
        pygame.draw.rect(surf, COLOR_GOAL, self.cell_to_rect(*self.goal))

        # grid overlay lines
        for r in range(self.rows+1):
            y = self.offset_y + r * self.cell_h
            pygame.draw.line(surf, COLOR_GRID_LINE, (self.offset_x, y), (self.offset_x + self.cols*self.cell_w, y))
        for c in range(self.cols+1):
            x = self.offset_x + c * self.cell_w
            pygame.draw.line(surf, COLOR_GRID_LINE, (x, self.offset_y), (x, self.offset_y + self.rows*self.cell_h))
