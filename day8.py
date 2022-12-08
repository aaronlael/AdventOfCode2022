from input.day8 import test, inp

def solution1(inp: str) -> int:
    treerows = inp.split("\n")
    visibletrees = 0
    for y in range(len(treerows)):
        for x in range(len(treerows[0])):
            if y == 0 or y == (len(treerows) - 1) or x == 0 or x == (len(treerows[0]) - 1):
                visibletrees += 1
            else:
                if max(treerows[y][:x]) < treerows[y][x] or max(treerows[y][x+1:]) < treerows[y][x]:
                    visibletrees += 1
                else:
                    yrow = [tree[x] for tree in treerows]
                    if max(yrow[:y]) < yrow[y] or max(yrow[y+1:]) < yrow[y]:
                        visibletrees += 1
    return visibletrees


print("test solution p1")
print(solution1(test))
print("solution p1")
print(solution1(inp))


def solution2(inp: str) -> int:
    treerows = inp.split("\n")
    maxscenicscore = 0
    for y in range(len(treerows)):
        for x in range(len(treerows[0])):
            currentscenicscore = []
            directionscore = 0
            height = int(treerows[y][x])
            # look left
            wx = x
            wy = y
            while wx >= 1:
                wx -= 1
                if int(treerows[y][wx]) < height:
                    directionscore += 1
                else:
                    directionscore += 1
                    break

            currentscenicscore.append(directionscore)
            directionscore = 0
            wx = x
            # look right
            while wx <= len(treerows[0]) - 2:
                wx += 1
                if int(treerows[y][wx]) < height:
                    directionscore += 1
                else:
                    directionscore += 1
                    break

            currentscenicscore.append(directionscore)
            directionscore = 0
            # look up
            while wy >= 1:
                wy -= 1
                if int(treerows[wy][x]) < height:
                    directionscore += 1
                else:
                    directionscore += 1
                    break

            currentscenicscore.append(directionscore)
            directionscore = 0
            wy = y
            # look down
            while wy <= len(treerows) - 2:
                wy += 1
                if int(treerows[wy][x]) < height:
                    directionscore += 1
                else:
                    directionscore += 1
                    break

            currentscenicscore.append(directionscore)
            cs = currentscenicscore[0] * currentscenicscore[1] * currentscenicscore[2] * currentscenicscore[3]
            if cs > maxscenicscore:
                maxscenicscore = cs
    return maxscenicscore
            
print("test solution p2")
print(solution2(test))
print("solution p2")
print(solution2(inp))