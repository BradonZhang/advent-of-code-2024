from pathlib import Path
from collections import deque


with ((Path(__file__).parent.parent.parent) / "data" / "20.in").open() as f:
    grid = f.read().strip().splitlines()

D = [(0, 1), (1, 0), (0, -1), (-1, 0)]
S = next((i, j) for i, line in enumerate(grid) if (j := line.find("S")) != -1)
E = next((i, j) for i, line in enumerate(grid) if (j := line.find("E")) != -1)
m = len(grid)
n = len(grid[0])

bfs = deque([E])
dist_to_end = {E: 0}
while bfs:
    r0, c0 = bfs.popleft()
    for dr, dc in D:
        r1, c1 = r0 + dr, c0 + dc
        if grid[r1][c1] != "#" and (r1, c1) not in dist_to_end:
            bfs.append((r1, c1))
            dist_to_end[r1, c1] = dist_to_end[r0, c0] + 1
bfs = deque([S])
dist_from_start = {S: 0}
while bfs:
    r0, c0 = bfs.popleft()
    for dr, dc in D:
        r1, c1 = r0 + dr, c0 + dc
        if grid[r1][c1] != "#" and (r1, c1) not in dist_from_start:
            bfs.append((r1, c1))
            dist_from_start[r1, c1] = dist_from_start[r0, c0] + 1
assert dist_from_start[E] == dist_to_end[S]

cutoff = dist_to_end[S] - 100

p1 = 0
for r in range(1, m - 1):
    for c in range(1, n - 1):
        if grid[r][c] != "#":
            continue
        start_dist = float("inf")
        best_d = 0
        for d in range(4):
            dr, dc = D[d]
            r1, c1 = r + dr, c + dc
            if grid[r1][c1] == "#" or (r1, c1) not in dist_from_start:
                continue
            if (cand := 2 + dist_from_start[r1, c1]) < start_dist:
                start_dist = cand
                best_d = d
        for dj in range(4):
            djr, djc = D[dj]
            rj, cj = r + djr, c + djc
            if grid[rj][cj] == "#" or (rj, cj) not in dist_to_end:
                continue
            if start_dist + dist_to_end[rj, cj] <= cutoff:
                p1 += 1
print(p1)


p2 = 0
for r in range(1, m - 1):
    for c in range(1, n - 1):
        if (r, c) not in dist_from_start:
            continue
        bfs = deque([(r, c)])
        seen = {(r, c)}
        level = 0
        rem = 1
        while bfs:
            r1, c1 = bfs.popleft()
            if (r1, c1) in dist_to_end:
                assert grid[r1][c1] != "#"
                t = dist_to_end[r1, c1] + level + dist_from_start[r, c]
                if t <= cutoff:
                    p2 += 1
            for dr, dc in D:
                r2, c2 = r1 + dr, c1 + dc
                if (r2, c2) in seen:
                    continue
                if not (0 < r2 < m - 1) or not (0 < c2 < n - 1):
                    continue
                seen.add((r2, c2))
                bfs.append((r2, c2))
            rem -= 1
            if rem == 0:
                level += 1
                rem = len(bfs)
                if level > 20:
                    break
print(p2)
