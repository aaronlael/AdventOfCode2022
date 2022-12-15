from input.day15 import test, inp

class sensor():
    def __init__(self, x: int, y: int, manhattan_dist: int):
        self.x = x
        self.y = y
        self.manhattan_dist = manhattan_dist
    
    def check_coord(self, coord: tuple) -> bool:
        return (abs(self.x - coord[0]) + abs(self.y - coord[1])) <= self.manhattan_dist

    def visible_row(self, y_axis: int) ->list:
        v_row = []
        if abs(self.y - y_axis) <= self.manhattan_dist:
            remaining_manhattan = self.manhattan_dist - abs(self.y - y_axis)
            end_x = self.x + remaining_manhattan
            start_x = self.x - remaining_manhattan
            for vx in range(start_x, end_x + 1):
                v_row.append((vx, y_axis)) 

        return v_row

    def vision(self, y_axis: int) -> tuple:
        if abs(self.y - y_axis) <= self.manhattan_dist:
            remaining_manhattan = self.manhattan_dist - abs(self.y - y_axis)
            end_x = self.x + remaining_manhattan
            start_x = self.x - remaining_manhattan
            return (start_x, end_x)
        return (-1, -1)
        

def sensors_list(inp: str) -> dict:
    sensors = []
    beacons = []
    inp = inp.split("\n")
    for row in inp:
        row = row.split(" ")
        sensor_x = int(row[2].split("=")[-1][:-1])
        sensor_y = int(row[3].split("=")[-1][:-1])
        beacon_x = int(row[8].split("=")[-1][:-1])
        beacon_y = int(row[9].split("=")[-1])
        manhattan_dist = abs(sensor_x - beacon_x) + abs(sensor_y - beacon_y)
        sensors.append(sensor(sensor_x, sensor_y, manhattan_dist))
        beacons.append((beacon_x, beacon_y))
    sensor_map = {}
    sensor_map['sensors'] = sensors
    sensor_map['beacons'] = beacons

    return sensor_map


def row_check(sensor_map: dict, row_number: int) -> int:
    seen_points = []
    for sensor in sensor_map['sensors']:
        seen_points += sensor.visible_row(row_number)
    seen_points = list(set(seen_points))
    for beacon in sensor_map['beacons']:
        if beacon in seen_points:
            seen_points.pop(seen_points.index(beacon))
    return len(seen_points)
    


print("test solution p1")
print(row_check(sensors_list(test), 10))
print("solution p1")
print(row_check(sensors_list(inp), 2000000))       


def row_check2(sensor_map: dict, row_number: int, max_col: int) -> tuple:
    number_chunks = [(0,max_col)]
    for sensor in sensor_map['sensors']:
        if len(number_chunks) == 0:
            return (-1, -1)
        sensor_vision = sensor.vision(row_number)
        chunks_to_pop = []
        for i in range(len(number_chunks)):
            nc = number_chunks[i]
            if sensor_vision[0] > nc[1] or sensor_vision[1] < nc[0] or len(sensor_vision) == 0:
                continue
            else:
                if sensor_vision[0] <= nc[0]:
                    if sensor_vision[1] < nc[1]:
                        number_chunks[i] = (sensor_vision[1] + 1, nc[1])
                    elif sensor_vision[1] >= nc[1]:
                        chunks_to_pop.append(i)
                else:
                    number_chunks[i] = (nc[0], sensor_vision[0] - 1)
                    if sensor_vision[1] >= nc[1]:
                        continue
                    else:
                        number_chunks.append((sensor_vision[1] + 1, nc[1]))
        for idx in chunks_to_pop[::-1]:
            number_chunks.pop(idx)
    if len(number_chunks) > 0:
        return (number_chunks[0][0], row_number)
                        
def beacon_finder(sensor_map: dict, max_idx: int) -> int:
    for y in range(max_idx + 1):
        coords = row_check2(sensor_map, y, max_idx)
        if coords != (-1,-1) and coords != None:
            return (coords[0] * 4000000) + coords[1]

            
        
print("test solution p2")
print(beacon_finder(sensors_list(test), 20))
print("solution p2")
print(beacon_finder(sensors_list(inp), 4000000))    









