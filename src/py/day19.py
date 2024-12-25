from pathlib import Path
from functools import cache


with ((Path(__file__).parent.parent.parent) / "data" / "19.in").open() as f:
    alphabet, text = f.read().strip().split('\n\n')
    tokens = set(alphabet.split(', '))
    lines = text.splitlines()

@cache
def possible(search: str):
    if not search:
        return 1
    total = int(search in tokens)
    for i in range(1, len(search)):
        if search[:i] in tokens:
            total += possible(search[i:])
    return total

print(sum(possible(line) > 0 for line in lines))
print(sum(possible(line) for line in lines))
