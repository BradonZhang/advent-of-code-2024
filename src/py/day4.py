import re
from pathlib import Path

with ((Path(__file__).parent.parent.parent) / "data" / "4.in").open() as f:
    grid = f.read().strip()

n = grid.find("\n")

delin = "(\\n|.){{{}}}"
patterns = [
    delin.format(n + 1).join("XMAS"),
    delin.format(n).join("XMAS"),
    delin.format(n - 1).join("XMAS"),
    "XMAS",
    "SAMX",
    delin.format(n - 1).join("SAMX"),
    delin.format(n).join("SAMX"),
    delin.format(n + 1).join("SAMX"),
]
print(sum(len(re.findall(f"(?=({pattern}))", grid)) for pattern in patterns))

delin = delin.format(n - 1)
patterns = [
    delin.join(["M.M", "A", "S.S"]),
    delin.join(["S.M", "A", "S.M"]),
    delin.join(["S.S", "A", "M.M"]),
    delin.join(["M.S", "A", "M.S"]),
]
print(sum(len(re.findall(f"(?=({pattern}))", grid)) for pattern in patterns))
