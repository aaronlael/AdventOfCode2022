from input.day1 import test, inp

def part1(inp: str) -> int:
    inp = inp.split("\n\n")
    return max([sum([int(y) for y in x.split("\n")]) for x in inp])


print("test solution p1")
print(part1(test))
print("solution p1")
print(part1(inp))


def part2(inp: str) -> int:
    inp = inp.split("\n\n")
    return sum(sorted([sum([int(y) for y in x.split("\n")]) for x in inp], reverse=True)[:3])


print("test solution p2")
print(part2(test))
print("solution p2")
print(part2(inp))