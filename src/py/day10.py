from pathlib import Path
from functools import cache

with ((Path(__file__).parent.parent.parent) / "data" / "10.in").open() as f:
    grid = f.read().strip().splitlines()

m = len(grid)
n = len(grid[0])

D = [(1, 0), (0, 1), (-1, 0), (0, -1)]


@cache
def visit(r: int, c: int) -> tuple[set[tuple[int, int]], int]:
    if grid[r][c] == '9':
        return {(r, c)}, 1
    p1, p2 = set(), 0
    for dr, dc in D:
        r1 = r + dr
        c1 = c + dc
        if (
            0 <= (r1 := r + dr) < m
            and 0 <= (c1 := c + dc) < n
            and ord(grid[r1][c1]) == ord(grid[r][c]) + 1
        ):
            a, b = visit(r1, c1)
            p1 |= a
            p2 += b
    return p1, p2


p1 = 0
p2 = 0
for r in range(m):
    for c in range(n):
        if grid[r][c] == '0':
            a, b = visit(r, c)
            p1 += len(a)
            p2 += b

print(p1)
print(p2)
