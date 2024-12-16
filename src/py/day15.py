from pathlib import Path
from collections import deque
from copy import deepcopy


with ((Path(__file__).parent.parent.parent) / "data" / "15.in").open() as f:
    grid_raw, instructions = f.read().strip().split("\n\n")
    instructions = instructions.replace('\n', '')
    grid0 = [list(line) for line in grid_raw.splitlines()]

D = [(0, 1), (1, 0), (0, -1), (-1, 0)]
dkey = '>v<^'
m = len(grid0)
n = len(grid0[0])
robot0 = next((i, j) for i in range(m) for j in range(n) if grid0[i][j] == '@')

robot = robot0
grid = deepcopy(grid0)
for ins in instructions:
    # print('\n'.join(''.join(line) for line in grid))
    # print(ins)
    r, c = robot
    assert grid[r][c] == '@'
    d = dkey.index(ins)
    dr, dc = D[d]
    r0 = r1 = r + dr
    c0 = c1 = c + dc
    while grid[r1][c1] == 'O':
        r1 += dr
        c1 += dc
    if grid[r1][c1] == '#':
        continue
    grid[r1][c1], grid[r0][c0], grid[r][c] = grid[r0][c0], grid[r][c], grid[r1][c1]
    robot = r0, c0

p1 = 0
for i in range(m):
    for j in range(n):
        if grid[i][j] == 'O':
            p1 += 100 * i + j
print(p1)

n *= 2
grid2 = []
xx_map = {'.': '..', '#': '##', 'O': '[]', '@': '@.'}
for row in grid0:
    # print(row)
    grid2.append([])
    for x in row:
        grid2[-1].extend(xx_map[x])

robot = (robot0[0], robot0[1] * 2)
for ins in instructions:
    # print(ins)
    # print('\n'.join(''.join(line) for line in grid2))
    # print(robot)
    r, c = robot
    # print(grid2[r])
    assert grid2[r][c] == '@'
    d = dkey.index(ins)
    dr, dc = D[d]
    r0, c0 = r + dr, c + dc
    if dr == 0:
        c1 = c0
        while grid2[r][c1] in '[]':
            c1 += dc
        if grid2[r][c1] == '.':
            while grid2[r][c1] != '@':
                grid2[r][c1] = grid2[r][c1 - dc]
                c1 -= dc
            grid2[r][c1] = '.'
            robot = r, c0
    else:
        if grid2[r0][c] == '.':
            grid2[r0][c] = '@'
            grid2[r][c] = '.'
            robot = r0, c
        elif grid2[r0][c] == '#':
            pass
        else:
            seen = {robot}
            dfs = deque(seen)
            hit_wall = False
            while dfs:
                # print('dfs', dfs)
                r1, c1 = dfs.pop()
                if grid2[r1][c1] == '.':
                    continue
                cands = [(r1 + dr, c1)]
                if grid2[r1][c1] == '[':
                    cands.append((r1, c1 + 1))
                elif grid2[r1][c1] == ']':
                    cands.append((r1, c1 - 1))
                elif grid2[r1][c1] == '#':
                    hit_wall = True
                    break
                for cand in cands:
                    if cand not in seen:
                        seen.add(cand)
                        dfs.append(cand)
            if not hit_wall:
                to_move = sorted(seen, reverse=dr > 0)
                # print('move', to_move)
                for r1, c1 in to_move:
                    # print(r1, c1)
                    # print('\n'.join(''.join(line) for line in grid2))
                    # print(robot)
                    if grid2[r1][c1] == '.':
                        continue
                    grid2[r1 + dr][c1], grid2[r1][c1] = grid2[r1][c1], grid2[r1 + dr][c1]
                robot = r0, c
                # print(r1, c1)
                # print('\n'.join(''.join(line) for line in grid2))
                # print(robot)

p2 = 0
# print('\n'.join(''.join(line) for line in grid2))
for i in range(m):
    for j in range(n):
        if grid2[i][j] == '[':
            p2 += 100 * i + j
print(p2)
