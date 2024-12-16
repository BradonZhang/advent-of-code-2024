from pathlib import Path
from functools import cache
import math

with ((Path(__file__).parent.parent.parent) / "data" / "11.in").open() as f:
    stones = [int(x) for x in f.read().strip().split()]


@cache
def num_stones(s, t):
    if t == 0:
        return 1
    if s == 0:
        return num_stones(1, t - 1)
    if (digits := 1 + int(math.log10(s))) % 2 == 0:
        a, b = divmod(s, 10 ** (digits // 2))
        return num_stones(a, t - 1) + num_stones(b, t - 1)
    return num_stones(2024 * s, t - 1)

p1 = sum(num_stones(stone, 25) for stone in stones)
print(p1)
p2 = sum(num_stones(stone, 75) for stone in stones)
print(p2)
exit()

T = 25
for t in range(T):
    next_stones = []
    for stone in stones:
        if stone == 0:
            next_stones.append(1)
        elif len(str(stone)) % 2 == 0:
            s = str(stone)
            a, b = s[: len(s) // 2], s[len(s) // 2 :]
            next_stones.append(int(a))
            next_stones.append(int(b))
        else:
            next_stones.append(stone * 2024)
    stones = next_stones

print(len(stones))
