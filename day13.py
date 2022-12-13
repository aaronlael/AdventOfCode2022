from input.day13 import test, inp
import copy

L = type([])
I = type(1)

def part1(inp: str) -> int:
    inp = inp.split("\n\n")
    correct_order_packets = []
    idx_counter = 1
    for pair in inp:
        left, right = (eval(x) for x in pair.split("\n"))
        while True:
            if len(left) > 0 and len(right) > 0:
                left, right, b = order_check(left, right)
                if b == True:
                    correct_order_packets.append(idx_counter)
                    idx_counter += 1
                    break
                elif b == False:
                    idx_counter += 1
                    break
            else:
                if len(left) > len(right):
                    idx_counter += 1
                    break
                if len(left) < len(right):
                    correct_order_packets.append(idx_counter)
                    idx_counter += 1
                    break
    return sum(correct_order_packets)


def order_check(left: list, right: list) -> tuple:
    if len(left) == 0 or len(right) == 0:
        if len(left) > len(right):
            return left, right, False
        elif len(right) > len(left):
            return left, right, True
        else:
            return left, right, None
    # both ints?
    if type(left[0]) == I == type(right[0]):
        l = left.pop(0)
        r = right.pop(0)
        if r > l:
            return left, right, True
        elif r < l:
            return left, right, False
        else:
            if len(left) > 0 and len(right) > 0 and r == l:
                return left, right, None
            elif len(left) == 0 and len(right) > 0:

                return left, right, True
            elif len(right) == 0 and len(left) > 0:
                return left, right, False
            else:
                return left, right, None


    # both lists?
    elif type(left[0]) == L == type(right[0]):
        sl = left.pop(0)
        sr = right.pop(0)
        while True:
            sl, sr, order = order_check(sl, sr)
            if order in [True, False]:
                return left, right, order
            elif len(sl) == 0 and len(sr) > 0:
                return left, right, True
            elif len(sr) == 0 and len(sl) > 0:
                return left, right, False
            elif len(sr) == 0 == len(sl):
                return left, right, None
    # type mismatch correction
    elif type(left[0]) != type(right[0]):
        if type(left[0]) != L:
            left[0] = [left[0]]
        elif type(right[0]) != L:
            right[0] = [right[0]]
        return left, right, None

print("test solution p1")
print(part1(test))
print("solution p1")
print(part1(inp))



def part2(inp: str) -> int:
    """reuses ordercheck() from p1"""
    inp = '\n'.join(inp.split("\n\n")).split("\n") + ["[[2]]"] + ["[[6]]"]
    correct_order_packets = []
    for packet in inp:
        packet = eval(packet)
        if len(correct_order_packets) == 0:
            correct_order_packets.append(packet)
        else:
            for i in range(len(correct_order_packets)):
                left = copy.deepcopy(packet)
                right = copy.deepcopy(correct_order_packets[i])
                while True:
                    if len(left) > 0 and len(right) > 0:
                        left, right, b = order_check(left, right)
                        # packet before correct_order_packets[i]
                        if b == True:
                            correct_order_packets = correct_order_packets[:i] + [packet] + correct_order_packets[i:]
                            break
                        # packet after correct_order_packets[i]
                        elif b == False:
                            break
                    else:
                        # packet before correct_order_packets[i]
                        if len(left) < len(right):
                            correct_order_packets = correct_order_packets[:i] + [packet] + correct_order_packets[i:]
                            break
                        # packet after correct_order_packets[i]
                        if len(left) > len(right):
                            break
                if packet in correct_order_packets:
                    break
            if packet not in correct_order_packets:
                correct_order_packets += [packet]
    return (correct_order_packets.index([[2]]) + 1) * (correct_order_packets.index([[6]]) + 1)


print("test solution p2")
print(part2(test))
print("solution p2")
print(part2(inp))