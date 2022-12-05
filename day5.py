from input.day5 import test, inp

def part1(inp: str) -> str:
    rows = {}
    for n in range(1,10):
        rows[n] = []

    crates, instructions = inp.split("\n\n")
    crates = crates.split("\n")
    for r in crates[:-1]:
        c, dr = 1, 1
        while c < len(r):
            if r[c] != " ":
                rows[dr] += [r[c]]
            c += 4
            dr += 1
    instructions = instructions.split("\n")
    for i in instructions:
        i = i.split(" ")
        qty = int(i[1])
        fr = int(i[3])
        to = int(i[5])
        rows[to] = rows[fr][:qty][::-1] + rows[to]
        rows[fr] = rows[fr][qty:]

    out = ""
    for j in range(1, 10):
        if len(rows[j]) > 0:
            out += rows[j][0]

    return out

print("test solution p1")
print(part1(test))
print("solution p1")
print(part1(inp))


def part2(inp: str) -> str:
    rows = {}
    for n in range(1,10):
        rows[n] = []

    crates, instructions = inp.split("\n\n")
    crates = crates.split("\n")
    for r in crates[:-1]:
        c, dr = 1, 1
        while c < len(r):
            if r[c] != " ":
                rows[dr] += [r[c]]
            c += 4
            dr += 1
    instructions = instructions.split("\n")
    for i in instructions:
        i = i.split(" ")
        qty = int(i[1])
        fr = int(i[3])
        to = int(i[5])
        rows[to] = rows[fr][:qty] + rows[to]
        rows[fr] = rows[fr][qty:]

    out = ""
    for j in range(1, 10):
        if len(rows[j]) > 0:
            out += rows[j][0]

    return out

print("test solution p2")
print(part2(test))
print("solution p2")
print(part2(inp))