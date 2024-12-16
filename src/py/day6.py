from pathlib import Path

with ((Path(__file__).parent.parent.parent) / "data" / "6.in").open() as f:
    grid = f.read().strip().splitlines()

X = len(grid[0])
Y = len(grid)

DX = [1, 0, -1, 0]
DY = [0, 1, 0, -1]

x0, y0 = next(
    iter((x, y) for y, line in enumerate(grid) if (x := line.find("^")) != -1)
)


def sim(bx: int | None = None, by: int | None = None):
    if by is not None and bx is not None and grid[by][bx] != ".":
        return 0
    d = 3
    x, y = x0, y0
    seen1 = {(x, y)}
    seen2 = {(x, y, d)}
    while True:
        dx, dy = DX[d], DY[d]
        x1, y1 = x + dx, y + dy
        if x1 < 0 or x1 >= X or y < 0 or y1 >= Y:
            return len(seen1)
        if grid[y1][x1] == "#" or (x1, y1) == (bx, by):
            d = (d + 1) % 4
        else:
            x, y = x1, y1
        if (x, y, d) in seen2:
            return None
        seen1.add((x, y))
        seen2.add((x, y, d))

p1 = sim()
print(p1)

p2 = sum(sim(bx, by) is None for bx in range(X) for by in range(Y))
print(p2)
