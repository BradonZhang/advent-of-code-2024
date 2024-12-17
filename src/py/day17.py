from pathlib import Path
import re


with ((Path(__file__).parent.parent.parent) / "data" / "17.in").open() as f:
    a, b, c, *program = map(int, re.findall(r"\d+", f.read()))


def run(a, b=None, c=None):
    out = []
    while a != 0:
        out.append(((a // (1 << ((a & 7) ^ 5))) ^ 3 ^ (a & 7)) & 7)
        a >>= 3
    return out

    # Original program
    ip = 0
    out = []
    while ip < len(program) - 1:
        ins = program[ip]
        op = program[ip + 1]
        cb = (0, 1, 2, 3, a, b, c)[op]
        if ins == 0:
            a //= 2**cb
        elif ins == 1:
            b ^= op
        elif ins == 2:
            b = cb % 8
        elif ins == 3:
            if a != 0:
                ip = op
                continue
        elif ins == 4:
            b ^= c
        elif ins == 5:
            out.append(cb % 8)
        elif ins == 6:
            b = a // 2**cb
        elif ins == 7:
            c = a // 2**cb
        ip += 2
    return out

print(",".join(map(str, run(a, b, c))))

a_ = 0
for i in range(len(program) - 1, -1, -1):
    expect = program[i:]
    # print(expect)
    a = 0
    while run(a2 := a_ * 8 + a) != expect:
        a += 1
    # print(a, a_)
    a_ = a2
print(a_)
