from input.day12 import test, inp

ALPHA = "SabcdefghijklmnopqrstuvwxyzE"

def mazerunner(inp) -> int:
    inp = [list(x) for x in inp.split("\n")]
    bfsmatrix = [[0 for col in range(len(inp[0]))] for row in range(len(inp))]
    for y in range(len(inp)):
        for x in range(len(inp[y])):
            if inp[y][x] == "S":
                start = (y, x)
            elif inp[y][x] == "E":
                end = (y, x)

    bfsmatrix[start[0]][start[1]] = 1
    stepcount = 1
    while True:
        bfsmatrix = step(stepcount, bfsmatrix, inp)
        stepcount += 1
        if bfsmatrix[end[0]][end[1]] != 0:
            return bfsmatrix[end[0]][end[1]] - 1
   

def step(stepcount: int, bfsmatrix: list, inp: list) -> list:
    for y in range(len(bfsmatrix)):
        for x in range(len(bfsmatrix[y])):
            if bfsmatrix[y][x] == stepcount:
                for offset in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                    if 0 <= y + offset[0] <= len(bfsmatrix) - 1 and 0 <= x + offset[1] <= len(bfsmatrix[y]) - 1 and bfsmatrix[y+offset[0]][x+offset[1]] == 0:
                        if ALPHA.find(inp[y+offset[0]][x+offset[1]]) - ALPHA.find(inp[y][x]) <= 1:
                            bfsmatrix[y+offset[0]][x+offset[1]] = stepcount + 1
    return bfsmatrix



print("test solution p1")
print(mazerunner(test))
print("solution p1")
print(mazerunner(inp))


def mazerunner2(inp) -> int:
    inp = [list(x) for x in inp.split("\n")]
    possiblestarts = []
    for y in range(len(inp)):
        for x in range(len(inp[y])):
            if inp[y][x] == "S" or inp[y][x] == "a":
                possiblestarts.append((y, x))
            elif inp[y][x] == "E":
                end = (y, x)
    mindist = 423
    for start in possiblestarts:
        bfsmatrix = [[0 for _ in range(len(inp[0]))] for _ in range(len(inp))]
        bfsmatrix[start[0]][start[1]] = 1
        stepcount = 1
        while True:
            bfsmatrix, newchanges = step2(stepcount, bfsmatrix, inp)
            if newchanges == 0:
                break
            stepcount += 1
            if bfsmatrix[end[0]][end[1]] != 0:
                if bfsmatrix[end[0]][end[1]] - 1 < mindist:
                    mindist = bfsmatrix[end[0]][end[1]] - 1
    return mindist

def step2(stepcount: int, bfsmatrix: list, inp: list) -> tuple:
    changes = 0
    for y in range(len(bfsmatrix)):
        for x in range(len(bfsmatrix[y])):
            if bfsmatrix[y][x] == stepcount:
                for offset in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                    if 0 <= y + offset[0] <= len(bfsmatrix) - 1 and 0 <= x + offset[1] <= len(bfsmatrix[y]) - 1 and bfsmatrix[y+offset[0]][x+offset[1]] == 0:
                        if ALPHA.find(inp[y+offset[0]][x+offset[1]]) - ALPHA.find(inp[y][x]) <= 1:
                            bfsmatrix[y+offset[0]][x+offset[1]] = stepcount + 1
                            changes += 1
    return bfsmatrix, changes


print("test solution p2")
print(mazerunner2(test))
print("solution p2")
print(mazerunner2(inp))