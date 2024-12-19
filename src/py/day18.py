from pathlib import Path
import re
from collections import deque


with ((Path(__file__).parent.parent.parent) / "data" / "18.in").open() as f:
    fallen_bytes = [tuple(int(x) for x in line.split(',')) for line in f.read().splitlines()]

MAX = 70
P1T = 1024

D = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def get_dist(num_bytes: int):
    blocked = set(fallen_bytes[:num_bytes])
    dists = {(0, 0): 0}
    bfs = deque([(0, 0)])
    left = 1
    level = 0
    while bfs:
        x, y = bfs.popleft()
        for dx, dy in D:
            x1, y1 = x + dx, y + dy
            if (x1, y1) not in dists and (x1, y1) not in blocked and 0 <= x1 <= MAX and 0 <= y1 <= MAX:
                dists[x1, y1] = level + 1
                bfs.append((x1, y1))
        left -= 1
        if left == 0:
            left = len(bfs)
            level += 1
    return dists.get((MAX, MAX))


p1 = get_dist(P1T)
print(p1)


lo = P1T + 1
hi = len(fallen_bytes)

while lo < hi:
    mid = (lo + hi) // 2
    if get_dist(mid) is None:
        hi = mid
    else:
        lo = mid + 1

p2 = fallen_bytes[lo - 1]
print(p2)
