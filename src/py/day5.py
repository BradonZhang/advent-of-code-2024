from collections import defaultdict
from pathlib import Path

with ((Path(__file__).parent.parent.parent) / "data" / "5.in").open() as f:
    rules_text, updates_text = f.read().strip().split("\n\n")

rules = [tuple(map(int, line.split("|"))) for line in rules_text.splitlines()]
deps = defaultdict(set)
revdeps = defaultdict(set)
for a, b in rules:
    deps[b].add(a)
    revdeps[a].add(b)

updates = [list(map(int, line.split(","))) for line in updates_text.splitlines()]

p1 = 0
p2 = 0

for update in updates:
    U = set(update)
    todo = set(update)
    for num in update:
        if deps[num] & todo:
            break
        todo.remove(num)
    else:
        p1 += update[len(update) // 2]
        continue
    order = []
    minideps = {num: deps[num] & U for num in update}

    def next_leaf():
        return next(
            iter(
                key for key in minideps.keys() if key not in order and not minideps[key]
            ),
            None,
        )

    leaf = next_leaf()
    while leaf is not None:
        order.append(leaf)
        for key in minideps.keys():
            minideps[key].discard(leaf)
        leaf = next_leaf()
    p2 += order[len(order) // 2]

print(p1)
print(p2)
