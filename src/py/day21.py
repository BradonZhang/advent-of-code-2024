from pathlib import Path
from functools import cache

with ((Path(__file__).parent.parent.parent) / "data" / "21.in").open() as f:
    codes = f.read().strip().splitlines()

keypad = "789456123 0A"
dpad = " ^A<v>"


def nav(start: str, end: str, pad: str = dpad) -> list[str]:
    r0, c0 = divmod(pad.find(start), 3)
    r1, c1 = divmod(pad.find(end), 3)
    rx, cx = divmod(pad.find(' '), 3)
    dr = r1 - r0
    dc = c1 - c0
    v = "^" if dr < 0 else "v"
    h = "<" if dc < 0 else ">"
    options = []
    if c0 != cx or r1 != rx:
        options.append(v * abs(dr) + h * abs(dc) + "A")
    if r0 != rx or c1 != cx:
        option = h * abs(dc) + v * abs(dr) + "A"
        if not options or options[0] != option:
            options.append(option)
    return options


@cache
def dpad_score(ds: str, levels: int):
    if levels == 0:
        return len(ds)
    score = 0
    rob = "A"
    for d in ds:
        score += min(dpad_score(ds_, levels - 1) for ds_ in nav(rob, d))
        rob = d
    return score


def complexity(code: str, p2: bool = False):
    code_num = int(code.replace("A", ""))
    score = 0
    rob = "A"
    for key in code:
        score += min(dpad_score(ds, 25 if p2 else 2) for ds in nav(rob, key, keypad))
        rob = key
    return score * code_num


p1 = sum(map(complexity, codes))
print(p1)

p2 = sum(complexity(code, True) for code in codes)
print(p2)
