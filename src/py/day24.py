At the problematic registers, I took a look at the logic gates that were
import operator


with ((Path(__file__).parent.parent.parent) / "data" / "24.in").open() as f:
    regs_text, gates_text = f.read().strip().split("\n\n")
    regs = {
        (tokens := line.split(": "))[0]: bool(int(tokens[1]))
        for line in regs_text.splitlines()
    }
    gates = [tuple(line.split()) for line in gates_text.splitlines()]

OPS = {
    "AND": operator.and_,
    "OR": operator.or_,
    "XOR": operator.xor,
}

remaining = len(gates)

while remaining:
    for a, op, b, _, out in gates:
        if out == "nrd":
            print(a, op, b, out)
            print(regs.get(a), regs.get(b))
        if out in regs:
            continue
        try:
            res = OPS[op](regs[a], regs[b])
            regs[out] = res
            remaining -= 1
        except KeyError:
            continue


p1 = int("".join(
    str(int(regs[reg]))
    for reg in sorted((reg for reg in regs if reg.startswith("z")), reverse=True)
), 2)
print(p1)

### PART 2 DOES NOT PRINT; WAS SOLVED MANUALLY ###

"""
Strategy:

By setting X = 0b111...111 and Y = 0, you can find anomalies in X + Y by running
Part 1 and comparing to expectation. This should also be done with
X = Y = 0b111...111.

Each place is roughly the same set of operations, where xi XOR yi = zi, and
xi AND yi is the carry for the next place, in case there is a 1 to carry.

At the problematic registers, I took a look at the logic gates that were
anomalous, and I swapped the output registers until the program ran with the
proper sum.
"""

# z_count = sum(reg.startswith('z') for reg in regs)
# print(''.join(str(i // 10) for i in range(z_count - 1, -1, -1)))
# print(''.join(str(i % 10) for i in range(z_count - 1, -1, -1)))
# print('=' * z_count)
# x = int(
#     "".join(
#         str(int(regs[reg]))
#         for reg in sorted((reg for reg in regs if reg.startswith("x")), reverse=True)
#     ),
#     2,
# )
# y = int(
#     "".join(
#         str(int(regs[reg]))
#         for reg in sorted((reg for reg in regs if reg.startswith("y")), reverse=True)
#     ),
#     2,
# )
# print(bin(x + y)[2:].zfill(z_count))
# print(bin(p1)[2:].zfill(z_count))

# breakpoint()
