from input.day7 import test, inp

def solution1(inp: str) -> int:
    inp = inp.split("\n")
    dirmap = {"/": 
        {
        "subdirs" : [],
        "directsize" : 0
        }
    }
    currentdir = "/"
    for i in inp:
        if i[0] == "$":
            if i[2:4] == "cd":
                if i.split(" ")[-1] == "..":
                    for k in dirmap:
                        if currentdir in dirmap[k]["subdirs"]:
                            currentdir = k
                elif i.split(" ")[-1] == "/":
                    currentdir = "/"
                else:
                    if currentdir != "/":
                        currentdir = currentdir + "/" + i.split(" ")[-1]
                    else:
                        currentdir = currentdir + i.split(" ")[-1]
                    if currentdir not in dirmap:
                        dirmap[currentdir] = {
                            "subdirs" : [],
                            "directsize" : 0
                            }
            else:
                continue
        else:
            if i[:3] == "dir":
                if currentdir != "/":
                    dirmap[currentdir]["subdirs"].append(currentdir + "/" + i.split(" ")[-1])
                else:
                    dirmap[currentdir]["subdirs"].append(currentdir + i.split(" ")[-1])
            else:
                dirmap[currentdir]["directsize"] += int(i.split(" ")[0])
    out = 0
    cache = {}
    for k in dirmap:
        t = subparse1(k, dirmap, cache)
        cache[k] = t
        if t <= 100000:
            out += t
    return out


def subparse1(dir: str, dirmap: dict, cache: dict) -> int:
    val = dirmap[dir]["directsize"]
    dirs = dirmap[dir]["subdirs"]
    while len(dirs) > 0:
        if val > 100000:
            return val
        sd = dirs.pop(0)
        if sd not in cache:
            val += dirmap[sd]["directsize"]
            dirs += dirmap[sd]["subdirs"]
        else:
            val += cache[sd]

    return val




print("test solution p1")
print(solution1(test))
print("solution p1")
print(solution1(inp))

def solution2(inp: str) -> int:
    inp = inp.split("\n")
    dirmap = {"/": 
        {
        "subdirs" : [],
        "directsize" : 0
        }
    }
    currentdir = "/"
    for i in inp:
        if i[0] == "$":
            if i[2:4] == "cd":
                if i.split(" ")[-1] == "..":
                    for k in dirmap:
                        if currentdir in dirmap[k]["subdirs"]:
                            currentdir = k
                elif i.split(" ")[-1] == "/":
                    currentdir = "/"
                else:
                    if currentdir != "/":
                        currentdir = currentdir + "/" + i.split(" ")[-1]
                    else:
                        currentdir = currentdir + i.split(" ")[-1]
                    if currentdir not in dirmap:
                        dirmap[currentdir] = {
                            "subdirs" : [],
                            "directsize" : 0
                            }
            else:
                continue
        else:
            if i[:3] == "dir":
                if currentdir != "/":
                    dirmap[currentdir]["subdirs"].append(currentdir + "/" + i.split(" ")[-1])
                else:
                    dirmap[currentdir]["subdirs"].append(currentdir + i.split(" ")[-1])
            else:
                dirmap[currentdir]["directsize"] += int(i.split(" ")[0])

    cache = {}
    for k in dirmap:
        cache[k] = subparse2(k, dirmap)

    remainingspace = 70000000 - cache["/"]
    neededspace = 30000000 - remainingspace
    spaces = [v for _,v in cache.items() if v >= neededspace]
    return min(spaces)


def subparse2(dir: str, dirmap: dict) -> int:
    val = dirmap[dir]["directsize"]
    dirs = dirmap[dir]["subdirs"]
    while len(dirs) > 0:
        sd = dirs.pop(0)
        val += dirmap[sd]["directsize"]
        dirs += dirmap[sd]["subdirs"]


    return val


print("test solution p2")
print(solution2(test))
print("solution2 p2")
print(solution2(inp))