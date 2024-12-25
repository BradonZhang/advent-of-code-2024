from pathlib import Path
from collections import deque, Counter


with ((Path(__file__).parent.parent.parent) / "data" / "22.in").open() as f:
    nums = [int(line) for line in f.read().strip().splitlines()]


def mixprune(secret: int, n: int):
    return (secret ^ n) % 16777216

ops = [
    lambda x: x * 64,
    lambda x: x // 32,
    lambda x: x * 2048,
]

def next_secret(secret: int):
    for op in ops:
        secret = mixprune(secret, op(secret))
    return secret

def nth_secret(secret: int, n: int):
    for _ in range(n):
        secret = next_secret(secret)
    return secret

def get_best_price(secret: int):
    history = deque(maxlen=4)
    seen = {}
    for _ in range(2000):
        ns = next_secret(secret)
        history.append((ns % 10) - (secret % 10))
        if len(history) == 4:
            key = tuple(history)
            if key not in seen:
                # print(key, ns % 10)
                seen[key] = ns % 10
        secret = ns
    return seen

p1 = sum(nth_secret(num, 2000) for num in nums)

overall = Counter()
for num in nums:
    overall.update(get_best_price(num))
p2 = overall.most_common(1)[0][1]
