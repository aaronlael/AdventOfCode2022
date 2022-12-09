from input.day9 import test, inp, test2

def part1(inp: str) -> int:
    inp = inp.split("\n")
    tail_has_been_here = []
    rope_positions = { 
        "H" : [0, 0],
        "T" : [0, 0]
    }
    for movement in inp:
        direction, quantity = movement.split(" ")
        quantity = int(quantity)
        for _ in range(quantity):
            previous_h = [x for x in rope_positions["H"]]
            if direction == "R":
                rope_positions["H"][0] += 1
            elif direction == "L":
                rope_positions["H"][0] -= 1
            elif direction == "U":
                rope_positions["H"][1] += 1
            elif direction == "D":
                rope_positions["H"][1] -= 1
            if not tailadjacent(rope_positions):
                rope_positions = updatetail(rope_positions, previous_h)
            tail_has_been_here.append(','.join([str(x) for x in rope_positions["T"]]))
    return len(set(tail_has_been_here))


def tailadjacent(rp: dict) -> bool:
    # Same Position
    if rp["H"] == rp["T"]:
        return True
    # Up, Down, Right, Left
    elif rp["T"] in [[rp["H"][0],rp["H"][1] + 1 ], [rp["H"][0],rp["H"][1] - 1 ], [rp["H"][0] + 1,rp["H"][1] ], [rp["H"][0] -1 ,rp["H"][1] ]]:
        return True
    # diagonals
    elif rp["T"] in [[rp["H"][0] + 1,rp["H"][1] + 1 ], [rp["H"][0] + 1,rp["H"][1] - 1 ], [rp["H"][0] - 1,rp["H"][1] + 1 ], [rp["H"][0] -1 ,rp["H"][1] -1]]:
        return True
    else:
        return False

def updatetail(rp: dict, ph: list) -> dict:
    # same row
    if rp["H"][0] == rp["T"][0]:
        if rp["H"][1] > rp["T"][1]:
            rp["T"][1] += 1
        else:
            rp["T"][1] -= 1
    # same column
    elif rp["H"][1] == rp["T"][1]:
        if rp["H"][0] > rp["T"][0]:
            rp["T"][0] += 1
        else:
            rp["T"][0] -= 1
    # different row and column
    else:
        rp["T"] = ph
    return rp




print("test solution p1")
print(part1(test))
print("solution p1")
print(part1(inp))


def part2(inp: str, knot_count: int) -> int:
    inp = inp.split("\n")
    tail_has_been_here = []
    rope_positions = { }
    for n in range(0,knot_count):
        rope_positions[n] = [0, 0]
    for movement in inp:
        direction, quantity = movement.split(" ")
        quantity = int(quantity)
        for _ in range(quantity):
            if direction == "R":
                rope_positions[0][0] += 1
            elif direction == "L":
                rope_positions[0][0] -= 1
            elif direction == "U":
                rope_positions[0][1] += 1
            elif direction == "D":
                rope_positions[0][1] -= 1
            for i in range(knot_count - 1):
                if not tailadjacent2(rope_positions, i, i+1):
                    if i == 0:
                        rope_positions = updatetail2(rope_positions, i, i+1)
                    else:
                        rope_positions = updatetail2(rope_positions, i, i+1)

            if i == knot_count - 2:
                    tail_has_been_here.append(','.join([str(x) for x in rope_positions[knot_count - 1]]))
    return len(set(tail_has_been_here))


def tailadjacent2(rp: dict, st: int, fn: int) -> bool:
    # Same Position
    if rp[st] == rp[fn]:
        return True
    # Up, Down, Right, Left
    elif rp[fn] in [[rp[st][0],rp[st][1] + 1 ], [rp[st][0],rp[st][1] - 1 ], [rp[st][0] + 1,rp[st][1] ], [rp[st][0] -1 ,rp[st][1] ]]:
        return True
    # diagonals
    elif rp[fn] in [[rp[st][0] + 1,rp[st][1] + 1 ], [rp[st][0] + 1,rp[st][1] - 1 ], [rp[st][0] - 1,rp[st][1] + 1 ], [rp[st][0] -1 ,rp[st][1] -1]]:
        return True
    else:
        return False

def updatetail2(rp: dict, h: int, t: int) -> dict:
    # same row
    if rp[h][0] == rp[t][0]:
        if rp[h][1] > rp[t][1]:
            rp[t][1] += 1
        else:
            rp[t][1] -= 1
    # same column
    elif rp[h][1] == rp[t][1]:
        if rp[h][0] > rp[t][0]:
            rp[t][0] += 1
        else:
            rp[t][0] -= 1
    # different row and column
    else:
        if rp[h][0] > rp[t][0]:
            rp[t][0] += 1
        else:
            rp[t][0] -= 1
        if rp[h][1] > rp[t][1]:
            rp[t][1] += 1
        else:
            rp[t][1] -= 1
    return rp


print("test solution p2")
print(part2(test, 10))
print("test2 solution p2")
print(part2(test2, 10))
print("solution p2")
print(part2(inp, 10))