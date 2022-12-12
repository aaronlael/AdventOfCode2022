from input.day10 import test, inp
import math

def cyclotron(inp: str) -> int:
    tracked_cycles = [20, 60, 100, 140, 180, 220]
    cycles = [x.split(" ") for x in inp.split("\n")]
    instructions = [1]
    for cycle in cycles:
        if cycle[0] == "noop":
            instructions.append(instructions[-1])
        elif cycle[0] == "addx":
            v = int(cycle[-1])
            instructions.append(instructions[-1])
            instructions.append(instructions[-1] + v)
    frequency_output = 0
    for tc in tracked_cycles:
        frequency_output += tc * instructions[tc-1]
    return frequency_output



print("test solution p1")
print(cyclotron(test))
print("solution p1")
print(cyclotron(inp))


def tubevision(inp: str) -> str:
    cycles = [x.split(" ") for x in inp.split("\n")]
    instructions = [1]
    for cycle in cycles:
        if cycle[0] == "noop":
            instructions.append(instructions[-1])
        elif cycle[0] == "addx":
            v = int(cycle[-1])
            instructions.append(instructions[-1])
            instructions.append(instructions[-1] + v)
    output = []
    icount = 0 
    for instruction in instructions:
        pixeloffset = math.floor((icount + 1) /40)
        if icount in range(instruction + (pixeloffset * 40) -1, instruction + (pixeloffset * 40) + 2):
            output.append("#")
        else:
            output.append(".")
        icount += 1
    ocount = 0
    while ocount < len(output):
        print(''.join(output[ocount:ocount+40]))
        ocount += 40
    return "Done"

print("test solution p2")
print(tubevision(test))
print("solution p2")
print(tubevision(inp))