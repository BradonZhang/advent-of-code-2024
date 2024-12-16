from collections import deque
from pathlib import Path


with ((Path(__file__).parent.parent.parent) / "data" / "12.in").open() as f:
    grid = f.read().strip().split()

m = len(grid)
n = len(grid[0])

D = [(0, 1), (1, 0), (0, -1), (-1, 0)]

p1 = 0
p2 = 0
seen = set()
for r in range(m):
    for c in range(n):
        if (r, c) in seen:
            continue
        seen.add((r, c))
        q = deque([(r, c)])
        a = 0
        edges = set()
        while q:
            r0, c0 = q.popleft()
            a += 1
            for d, (dr, dc) in enumerate(D):
                r1, c1 = r0 + dr, c0 + dc
                if 0 <= r1 < m and 0 <= c1 < n and grid[r1][c1] == grid[r0][c0]:
                    if (r1, c1) not in seen:
                        q.append((r1, c1))
                        seen.add((r1, c1))
                else:
                    edges.add((r0, c0, d))
        s = 0
        p1 += len(edges) * a
        while edges:
            edge = min(edges)
            q = deque([edge])
            edges.discard(edge)
            s += 1
            while q:
                r0, c0, d = q.popleft()
                dc, dr = D[d]
                r1, c1 = r0 + dr, c0 + dc
                r2, c2 = r0 - dr, c0 - dc
                for edge in [(r1, c1, d), (r2, c2, d)]:
                    if edge in edges:
                        q.append(edge)
                        edges.discard(edge)
        p2 += s * a
print(p1)
print(p2)
