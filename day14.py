from input.day14 import test, inp

def build_map(inp: str) -> list:
    """returns 2d list game map"""
    inp = inp.split("\n")
    points = []
    xcoords = [500]
    ycoords = [0]
    for row in inp:
        row = row.split(" -> ")
        for i in  range(len(row) - 1):
            # starting point of line
            x, y = [int(j) for j in row[i].split(",")]
            if x not in xcoords: xcoords.append(x)
            if y not in ycoords: ycoords.append(y)
            # ending point of line
            nx, ny = [int(j) for j in row[i+1].split(",")]
            if nx not in xcoords: xcoords.append(nx)
            if ny not in ycoords: ycoords.append(ny)
            if y == ny:
                if x > nx:
                    while x >= nx:
                        points.append((y, x))
                        x -= 1
                else:
                    while x <= nx:
                        points.append((y, x))
                        x += 1
            elif x == nx:
                if y > ny:
                    while y >= ny:
                        points.append((y, x))
                        y -= 1
                else:
                    while y <= ny:
                        points.append((y, x))
                        y += 1
    # bounds for game map
    max_y = max(ycoords)
    max_x = max(xcoords)

    game_map = [["." for _ in range(max_x + 1)] for _ in range(max_y + 1)]
    for point in points:
        game_map[point[0]][point[1]] = "#"
    
    return game_map

def drop_sand(game_map: list) -> int:
    sand_dropped = 0
    try:
        while True:
            current_sand_can_move = True
            # y, x coord
            sand_point = (0, 500)
            while current_sand_can_move:
                if game_map[sand_point[0] + 1][sand_point[1]] == ".":
                    sand_point = (sand_point[0] + 1,sand_point[1])
                else:
                    if game_map[sand_point[0] + 1][sand_point[1] - 1] == ".":
                       sand_point = (sand_point[0] + 1,sand_point[1] - 1)
                    elif game_map[sand_point[0] + 1][sand_point[1] + 1] == ".":
                        sand_point = (sand_point[0] + 1,sand_point[1] + 1)
                    else:
                        game_map[sand_point[0]][sand_point[1]] = "O"
                        current_sand_can_move = False
                        sand_dropped += 1


    except IndexError:
        return sand_dropped

print("test solution p1")
print(drop_sand(build_map(test)))
print("solution p1")
print(drop_sand(build_map(inp)))


def build_map2(inp: str) -> tuple:
    """returns 2d list game map"""
    inp = inp.split("\n")
    points = []
    xcoords = [500]
    ycoords = [0]
    for row in inp:
        row = row.split(" -> ")
        for i in  range(len(row) - 1):
            # starting point of line
            x, y = [int(j) for j in row[i].split(",")]
            if x not in xcoords: xcoords.append(x)
            if y not in ycoords: ycoords.append(y)
            # ending point of line
            nx, ny = [int(j) for j in row[i+1].split(",")]
            if nx not in xcoords: xcoords.append(nx)
            if ny not in ycoords: ycoords.append(ny)
            if y == ny:
                if x > nx:
                    while x >= nx:
                        points.append((y, x))
                        x -= 1
                else:
                    while x <= nx:
                        points.append((y, x))
                        x += 1
            elif x == nx:
                if y > ny:
                    while y >= ny:
                        points.append((y, x))
                        y -= 1
                else:
                    while y <= ny:
                        points.append((y, x))
                        y += 1
    # bounds for game map
    max_y = max(ycoords) + 2
    max_x = max(xcoords) + max_y

    game_map = [["." for _ in range(max_x + 1)] for _ in range(max_y + 1)]
    for point in points:
        game_map[point[0]][point[1]] = "#"
    
    return game_map, max_y -1


def drop_sand2(game_map: list, max_y: int) -> int:
    sand_dropped = 0
    while game_map[0][500] == ".":
        current_sand_can_move = True
        # y, x coord
        sand_point = (0, 500)
        while current_sand_can_move:
            if sand_point[0] == max_y:
                game_map[sand_point[0]][sand_point[1]] = "O"
                current_sand_can_move = False
                sand_dropped += 1
            if game_map[sand_point[0] + 1][sand_point[1]] == ".":
                sand_point = (sand_point[0] + 1,sand_point[1])
            else:
                if game_map[sand_point[0] + 1][sand_point[1] - 1] == ".":
                    sand_point = (sand_point[0] + 1,sand_point[1] - 1)
                elif game_map[sand_point[0] + 1][sand_point[1] + 1] == ".":
                    sand_point = (sand_point[0] + 1,sand_point[1] + 1)
                else:
                    game_map[sand_point[0]][sand_point[1]] = "O"
                    current_sand_can_move = False
                    sand_dropped += 1

    return sand_dropped

print("test solution p2")
print(drop_sand2(*build_map2(test)))
print("solution p2")
print(drop_sand2(*build_map2(inp)))