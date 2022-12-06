from input.day6 import test, inp

def solution(inp: str, size: int) -> int:
    chr = 0
    while True:
        if len(set(inp[chr:chr+size])) == len(inp[chr:chr+size]):
            return chr + size
        else:
            chr += 1


print("test solution p1")
print(solution(test, 4))
print("solution p1")
print(solution(inp, 4))

print("test solution p2")
print(solution(test, 14))
print("solution p2")
print(solution(inp, 14))