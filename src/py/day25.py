from pathlib import Path

with ((Path(__file__).parent.parent.parent) / "data" / "25.in").open() as f:
    chunks = [chunk.splitlines() for chunk in f.read().strip().split('\n\n')]
    locks = [chunk for chunk in chunks if chunk[0][0] == '#']
    keys = [chunk for chunk in chunks if chunk[0][0] == '.']

m = len(chunks[0])
n = len(chunks[0][0])

p1 = 0
for lock in locks:
    for key in keys:
        lh = [sum(lock[r][c] == '#' for r in range(m)) - 1 for c in range(n)]
        kh = [sum(key[r][c] == '#' for r in range(m)) - 1 for c in range(n)]
        p1 += max(map(sum, zip(lh, kh))) < m - 1
print(p1)
