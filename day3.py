from input.day3 import test, inp

ALPHA = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

def part1(inp: str) -> int:
    inp = inp.split("\n")
    out = 0
    for pack in inp:
        pset = set(pack)
        p1 = pack[:int(len(pack)/2)]
        p2 = pack[int(len(pack)/2):]
        for p in pset:
            if p in p1 and p in p2:
                out += ALPHA.find(p) + 1
    return out


print("test solution p1")
print(part1(test))
print("solution p1")
print(part1(inp))

def part2(inp: str) -> int:
    inp = inp.split("\n")
    out = 0
    for i in range(0, len(inp), 3):
        pset = set(inp[i])
        for p in pset:
            if p in inp[i] and p in inp[i+1] and p in inp[i+2]:
                out += ALPHA.find(p) + 1
    return out


print("test solution p2")
print(part2(test))
print("solution p2")
print(part2(inp))