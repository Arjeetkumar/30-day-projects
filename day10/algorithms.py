# algorithms.py
from collections import deque
import heapq

def neighbors(grid, r, c):
    R = len(grid)
    C = len(grid[0])
    for dr,dc in ((-1,0),(1,0),(0,-1),(0,1)):
        nr, nc = r+dr, c+dc
        if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] == 0:
            yield nr, nc

# BFS generator
def bfs(grid, start, goal):
    """
    Yields steps for visualization.
    Yields dicts: {'type':'visit'|'frontier'|'path'|'done', 'pos':(r,c), ...}
    """
    sr, sc = start
    gr, gc = goal
    q = deque()
    q.append((sr,sc))
    visited = set()
    visited.add((sr,sc))
    parent = {}

    yield {'type':'frontier', 'pos': (sr,sc)}
    while q:
        r,c = q.popleft()
        yield {'type':'visit', 'pos': (r,c)}
        if (r,c) == (gr,gc):
            # reconstruct path
            path = []
            cur = (r,c)
            while cur != (sr,sc):
                path.append(cur)
                cur = parent[cur]
            path.append((sr,sc))
            path.reverse()
            for p in path:
                yield {'type':'path', 'pos':p}
            yield {'type':'done', 'found': True}
            return
        for nr,nc in neighbors(grid, r, c):
            if (nr,nc) not in visited:
                visited.add((nr,nc))
                parent[(nr,nc)] = (r,c)
                q.append((nr,nc))
                yield {'type':'frontier', 'pos': (nr,nc)}
    yield {'type':'done', 'found': False}
    return

# DFS generator (iterative)
def dfs(grid, start, goal):
    sr, sc = start
    gr, gc = goal
    stack = [(sr,sc)]
    visited = set()
    parent = {}
    yield {'type':'frontier','pos':(sr,sc)}
    while stack:
        r,c = stack.pop()
        if (r,c) in visited:
            continue
        visited.add((r,c))
        yield {'type':'visit','pos':(r,c)}
        if (r,c) == (gr,gc):
            path = []
            cur = (r,c)
            while cur != (sr,sc):
                path.append(cur); cur = parent[cur]
            path.append((sr,sc)); path.reverse()
            for p in path: yield {'type':'path','pos':p}
            yield {'type':'done','found':True}
            return
        for nr,nc in neighbors(grid, r, c):
            if (nr,nc) not in visited:
                parent[(nr,nc)] = (r,c)
                stack.append((nr,nc))
                yield {'type':'frontier','pos':(nr,nc)}
    yield {'type':'done','found':False}
    return

# A* generator (Manhattan)
def heuristic(a, b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

def a_star(grid, start, goal):
    sr, sc = start
    gr, gc = goal
    open_heap = []
    entry_finder = {}
    gscore = {start: 0}
    fscore = {start: heuristic(start, goal)}
    heapq.heappush(open_heap, (fscore[start], start))
    entry_finder[start] = fscore[start]
    parent = {}
    visited = set()

    yield {'type':'frontier','pos': start}
    while open_heap:
        f, current = heapq.heappop(open_heap)
        if current in visited:
            continue
        visited.add(current)
        r,c = current
        yield {'type':'visit','pos':(r,c)}
        if current == goal:
            # reconstruct
            path = []
            cur = current
            while cur != start:
                path.append(cur); cur = parent[cur]
            path.append(start); path.reverse()
            for p in path: yield {'type':'path','pos':p}
            yield {'type':'done','found':True}
            return
        for nbr in neighbors(grid, r, c):
            tentative_g = gscore[current] + 1
            if tentative_g < gscore.get(nbr, 1e9):
                parent[nbr] = current
                gscore[nbr] = tentative_g
                f = tentative_g + heuristic(nbr, goal)
                fscore[nbr] = f
                heapq.heappush(open_heap, (f, nbr))
                entry_finder[nbr] = f
                yield {'type':'frontier','pos':nbr, 'f': f}
    yield {'type':'done','found':False}
    return
