import heapq
from pathlib import Path
from collections import deque


with ((Path(__file__).parent.parent.parent) / "data" / "16.in").open() as f:
    grid = f.read().strip().splitlines()

D = [(0, 1), (1, 0), (0, -1), (-1, 0)]
m = len(grid)
n = len(grid[0])
start = next((i, j, 0) for i, line in enumerate(grid) if (j := line.find("S")) >= 0)
end = next((i, j) for i, line in enumerate(grid) if (j := line.find("E")) >= 0)


pq = [(0, *start)]
bests = {start: (0, set())}
min_score = float("inf")
while pq:
    score, r, c, d = heapq.heappop(pq)
    prev_best = bests.get((r, c, d), (float("inf"),))[0]
    if prev_best < score:
        continue
    if (r, c) == end:
        min_score = min(min_score, score)
    dr, dc = D[d]
    cands = [
        (score + 1, r + dr, c + dc, d),
        (score + 1000, r, c, (d + 1) % 4),
        (score + 1000, r, c, (d - 1) % 4),
    ]
    for cand in cands:
        score1, r1, c1, d1 = cand
        if r1 < 0 or r1 >= m or c1 < 0 or c1 >= n or grid[r1][c1] == "#":
            continue
        key = (r1, c1, d1)
        best = bests.get(key, (float("inf"),))[0]
        if score1 <= best:
            if score1 < best:
                bests[key] = (score1, set())
                heapq.heappush(pq, cand)
            bests[key][1].add((r, c, d))
print(min_score)
bfs = deque(
    (*end, d)
    for d in range(4)
    if bests.get((*end, d), (float("inf"),))[0] == min_score
)
seen = {end}
while bfs:
    r, c, d = bfs.popleft()
    parents = bests.get((r, c, d))[1]
    for parent in parents:
        if parent not in seen:
            bfs.append(parent)
            seen.add(parent[:2])
print(len(seen))
