from input.day2 import test, inp

PLAYMAP = {
    "A" : 1,
    "B" : 2,
    "C" : 3,
    "X" : 1,
    "Y" : 2,
    "Z" : 3,
}

OUTCOMEMAP = {
    "A" : {
    "X" : 3,
    "Y" : 6,
    "Z" : 0,

    },
    "B" : {
    "X" : 0,
    "Y" : 3,
    "Z" : 6,
    },
    "C": {
    "X" : 6,
    "Y" : 0,
    "Z" : 3,
    }
}

def gamecounter(inp: str) -> int:
    score = 0
    inp = inp.split("\n")
    for r in inp:
        game = r.split(" ")
        score += OUTCOMEMAP[game[0]][game[1]] + PLAYMAP[game[1]]
    return score


print("test solution p1")
print(gamecounter(test))
print("solution p1")
print(gamecounter(inp))
    

PLAYMAP2 = {
    "X" : 0,
    "Y" : 3,
    "Z" : 6,
}

OUTCOMEMAP2 = {
    "A" : {
    "X" : 3,
    "Y" : 1,
    "Z" : 2,

    },
    "B" : {
    "X" : 1,
    "Y" : 2,
    "Z" : 3,
    },
    "C": {
    "X" : 2,
    "Y" : 3,
    "Z" : 1,
    }
}


def gamecounter2(inp: str) -> int:
    score = 0
    inp = inp.split("\n")
    for r in inp:
        game = r.split(" ")
        score += OUTCOMEMAP2[game[0]][game[1]] + PLAYMAP2[game[1]]
    return score


print("test solution p2")
print(gamecounter2(test))
print("solution p2")
print(gamecounter2(inp))