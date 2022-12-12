from input.day11 import test, inp
import math

class Monkey():
    def __init__(self, objects: list, operation: str, test: str, t: str, f: str, number: int, worryreduction: bool):
        self.number = number
        self.objects = objects
        self.operation = operation
        self.test = test
        self.t = t
        self.f = f
        self.inspectcount = 0
        self.currentobject = 0
        self.worryreduction = worryreduction

    def throw(self, monkeys: dict, monkeymod: int) -> None:
        self.inspect(monkeymod)
        if not self.currentobject % int(self.test):
            monkeys[self.t].objects.append(self.currentobject)
        else:
            monkeys[self.f].objects.append(self.currentobject)



    def inspect(self, monkeymod: int) -> None:
        self.inspectcount += 1
        self.currentobject = self.objects.pop()
        if self.operation[1] == "+":
            if self.operation[-1] == "old":
                self.currentobject += self.currentobject
            else:
                self.currentobject += int(self.operation[-1])
        else:
            if self.operation[-1] == "old":
                self.currentobject *= self.currentobject
            else:
                self.currentobject *= int(self.operation[-1])
        if self.worryreduction:
            self.currentobject = self.currentobject // 3
        else:
            self.currentobject %= monkeymod


def monkeyparse(inp: str, worryreduction: bool) -> dict:
    monkeys = {}
    inp = inp.split("\n\n")
    for monkey in inp:
        monkey = monkey.split("\n")
        monkeynumber = int(monkey[0][-2])
        monkeyitems = [int(x) for x in [y for y in monkey[1].split(": ")][-1].split(",")]
        monkeyoperation = monkey[2].split(" ")[-3:]
        monkeytest = monkey[3].split(" ")[-1]
        monkeyt = int(monkey[4].split(" ")[-1])
        monkeyf = int(monkey[5].split(" ")[-1])
        monkeys[monkeynumber] = Monkey(monkeyitems, monkeyoperation, monkeytest, monkeyt, monkeyf, monkeynumber, worryreduction)
    return monkeys


def monkeyloop(count: int, inp: str, worryreduction: bool) -> int:
    monkeys = monkeyparse(inp, worryreduction)
    monkeymod = math.prod([int(monkeys[x].test) for x in monkeys])
    for i in range(count):
        for monkey in monkeys:
            while len(monkeys[monkey].objects) > 0:
                monkeys[monkey].throw(monkeys, monkeymod)
    monkeybusiness = sorted([monkeys[x].inspectcount for x in monkeys], reverse=True)
    return monkeybusiness[0] * monkeybusiness[1]


print("test solution p1")
print(monkeyloop(20, test, True))
print("solution p1")
print(monkeyloop(20, inp, True))


print("test solution p2")
print(monkeyloop(10000, test, False))
print("solution p2")
print(monkeyloop(10000, inp, False))