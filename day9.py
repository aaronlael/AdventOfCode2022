from input.day9 import test, inp, test2

def part1(inp: str) -> int:
    inp = inp.split("\n")
    tailhasbeenhere = []
    ropepositions = { 
        "H" : [0, 0],
        "T" : [0, 0]
    }
    for movement in inp:
        direction, quantity = movement.split(" ")
        quantity = int(quantity)
        for _ in range(quantity):
            previous_h = [x for x in ropepositions["H"]]
            if direction == "R":
                ropepositions["H"][0] += 1
            elif direction == "L":
                ropepositions["H"][0] -= 1
            elif direction == "U":
                ropepositions["H"][1] += 1
            elif direction == "D":
                ropepositions["H"][1] -= 1
            if not tailadjacent(ropepositions):
                ropepositions = updatetail(ropepositions, previous_h)
            tailhasbeenhere.append(','.join([str(x) for x in ropepositions["T"]]))
    return len(set(tailhasbeenhere))


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


def part2(inp: str) -> int:
    inp = inp.split("\n")
    tailhasbeenhere = []
    ropepositions = { }
    for n in range(0,10):
        ropepositions[n] = [0, 0]
    for movement in inp:
        direction, quantity = movement.split(" ")
        quantity = int(quantity)
        for _ in range(quantity):
            if direction == "R":
                ropepositions[0][0] += 1
            elif direction == "L":
                ropepositions[0][0] -= 1
            elif direction == "U":
                ropepositions[0][1] += 1
            elif direction == "D":
                ropepositions[0][1] -= 1
            for i in range(9):
                if not tailadjacent2(ropepositions, i, i+1):
                    if i == 0:
                        ropepositions = updatetail2(ropepositions, i, i+1)
                    else:
                        ropepositions = updatetail2(ropepositions, i, i+1)

            if i == 8:
                    tailhasbeenhere.append(','.join([str(x) for x in ropepositions[9]]))
    return len(set(tailhasbeenhere))


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
print(part2(test))
print("test2 solution p2")
print(part2(test2))
print("solution p2")
print(part2(inp))