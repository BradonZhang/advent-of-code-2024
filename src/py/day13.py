import re
import sys
# from functools import cache
from pathlib import Path

import numpy as np

num_re = re.compile(r'\d+')

with ((Path(__file__).parent.parent.parent) / "data" / "13.in").open() as f:
    prizes = [
        tuple(int(x) for x in num_re.findall(chunk)) for chunk in f.read().split('\n\n')
    ]

INF = 10**9
ERR = 10000000000000

sys.setrecursionlimit(10000)


# def prize_dp(ax, ay, bx, by):
#     @cache
#     def dp(px, py):
#         if px == 0 and py == 0:
#             return 0
#         if px < 0 or py < 0:
#             return INF
#         return min(3 + dp(px - ax, py - ay), 1 + dp(px - bx, py - by))

#     return dp


# p1 = 0
# for ax, ay, bx, by, px, py in prizes:
#     print('hi')
#     dp = prize_dp(ax, ay, bx, by)
#     if dp(px, py) < INF:
#         p1 += dp(px, py)
#     dp.cache_clear()
# print(p1)

p1 = 0
for ax, ay, bx, by, px, py in prizes:
    ab = np.array([[ax, bx], [ay, by]], dtype=np.int64)
    p = np.array([px, py], dtype=np.int64)
    a, b = np.linalg.solve(ab, p)
    if (
        np.allclose(np.dot(ab, [a, b]), p)
        and (abs(a - round(a)) < 0.0001)
        and (abs(b - round(b)) < 0.0001)
    ):
        p1 += round(3 * a + b)
print(p1)


p2 = 0
for ax, ay, bx, by, px, py in prizes:
    px += ERR
    py += ERR
    # a = Fraction(py - px, ay * bx - ax * by)
    # b = Fraction(py - px, by * ax - bx * ay)
    # continue

    ab = np.array([[ax, bx], [ay, by]], dtype=np.int64)
    p = np.array([px, py], dtype=np.int64)
    a, b = np.linalg.solve(ab, p)
    if (
        np.allclose(np.dot(ab, [a, b]), p)
        and (abs(a - round(a)) < 0.0001)
        and (abs(b - round(b)) < 0.0001)
    ):
        p2 += round(3 * a + b)
print(p2)
