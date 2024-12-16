from pathlib import Path

with ((Path(__file__).parent.parent.parent) / "data" / "9.in").open() as f:
    data = f.read().strip()

mem: list[int | None] = [None] * sum(map(int, data))
i = 0
sizes: list[int] = []
for num2, count in enumerate(map(int, data)):
    if num2 % 2 == 0:
        mem[i : i + count] = [num2 // 2] * count
        sizes.append(count)
    i += count
# mem0 = copy.copy(mem)

i = 0
j = len(mem) - 1
while j >= i:
    if mem[i] is not None:
        i += 1
    elif mem[j] is None:
        j -= 1
    else:
        mem[i], mem[j] = mem[j], mem[i]

p1 = sum(i * num for i, num in enumerate(mem) if num is not None)
print(p1)

# mem = copy.copy(mem0)
# g = mem.index(None)
# i, j = g, len(mem) - 1
# while j >= i:
#     if mem[i] is not None:
#         i += 1
#     elif mem[j] is None:
#         j -= 1
#     else:
#         mem[i], mem[j] = mem[j], mem[i]

class Node:
    def __init__(self, id_: int | None, size: int):
        self.id = id_
        self.size = size
        self.next: Node | None = None
        self.prev: Node | None = None

    def __repr__(self):
        return f'{self.id} ({self.size})'


head = None
tail = None
nodes: dict[int, Node] = {}
for num2, count in enumerate(map(int, data)):
    if num2 % 2 == 0:
        node = Node(num2 // 2, count)
        nodes[node.id] = node
    else:
        node = Node(None, count)
    if head is None:
        head = node
    if tail is None:
        tail = node
    else:
        tail.next = node
        node.prev = tail
        tail = node

for node_id in range(len(nodes) - 1, 0, -1):
    node = nodes[node_id]
    gap = head
    while gap is not node:
        if gap.id is None and gap.size >= node.size:
            break
        gap = gap.next
    if gap is node:
        continue
    if gap.size > node.size:
        new_gap = Node(None, gap.size - node.size)
        gap.next.prev = new_gap
        new_gap.prev = gap
        new_gap.next = gap.next
        gap.next = new_gap
        gap.size = node.size
    gap.prev.next = node
    if node.next:
        node.next.prev = gap
    if gap.next is not node:
        gap.next.prev = node
        node.prev.next = gap
        node.prev, gap.prev = gap.prev, node.prev
        node.next, gap.next = gap.next, node.next
    else:
        gap.next = node.next
        node.prev = gap.prev
        node.next = gap
        gap.prev = node
    if gap.prev.id is None:
        gap.prev.size += gap.size
        gap.size = 0
        gap.prev.next = gap.next
        if gap.next:
            gap.next.prev = gap.prev
        gap = gap.prev
    if gap.next and gap.next.id is None:
        gap.size += gap.next.size
        gap.next.size = 0
        if gap.next.next:
            gap.next.next.prev = gap
            gap.next = gap.next.next

curr = head
i = 0
p2 = 0
while curr is not None:
    if curr.id is not None:
        for j in range(curr.size):
            p2 += i * curr.id
            i += 1
    else:
        i += curr.size
    curr = curr.next
print(p2)
