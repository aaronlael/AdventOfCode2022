from input.day4 import test, inp


def part1(inp: str) -> int:
    inp = inp.split("\n")
    count = 0
    for pair in inp:
        p1, p2 = pair.split(",")
        p1 = [int(x) for x in p1.split("-")]
        p2 = [int(x) for x in p2.split("-")]
        if (p1[0] >= p2[0] and p1[1] <= p2[1]) or (p2[0] >= p1[0] and p2[1] <= p1[1]):
            count += 1
    return count


print("test solution p1")
print(part1(test))
print("solution p1")
print(part1(inp))


def part2(inp: str) -> int:
    inp = inp.split("\n")
    count = 0
    for pair in inp:
        p1, p2 = pair.split(",")
        p1 = [int(x) for x in p1.split("-")]
        p2 = [int(x) for x in p2.split("-")]
        if (p1[0] >= p2[0] and p1[0] <= p2[1]) or (p1[1] >= p2[0] and p1[1] <= p2[1]) or (p2[0] >= p1[0] and p2[0] <= p1[1]) or (p2[1] >= p1[0] and p2[1] <= p1[1]):
            count += 1
    return count


print("test solution p2")
print(part2(test))
print("solution p2")
print(part2(inp))