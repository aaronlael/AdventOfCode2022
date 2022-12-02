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


def gamecounter(inp: str, omap: dict, pmap: dict) -> int:
    score = 0
    inp = inp.split("\n")
    for r in inp:
        game = r.split(" ")
        score += omap[game[0]][game[1]] + pmap[game[1]]
    return score


print("test solution p1")
print(gamecounter(test, OUTCOMEMAP, PLAYMAP))
print("solution p1")
print(gamecounter(inp, OUTCOMEMAP, PLAYMAP))

print("test solution p2")
print(gamecounter(test, OUTCOMEMAP2, PLAYMAP2))
print("solution p2")
print(gamecounter(inp, OUTCOMEMAP2, PLAYMAP2))