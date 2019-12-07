#!/usr/bin/env python
# Solution to the AOC2019 Challenge 11/12
# https://adventofcode.com/2019/day/6
from typing import Dict


class Body:
    def __init__(self, name):
        self.name = name
        self.children = []

    def check(self, depth=0):
        if self.children:
            return depth + sum(child.check(depth + 1) for child in self.children)
        else:
            return depth

    def path(self, target):
        if target in self.children:
            return [self]
        else:
            for child in self.children:
                route = child.path(target)
                if route:
                    route.insert(0, self)
                    return route
            return None

    def __repr__(self):
        return f"{self.name}"


class OrbitalMap:
    def __init__(self):
        self.bodies = dict()
        self.check_sum = 0

    def analyze(self, string):
        base, orbit = string.split(")")
        self.add(base, orbit)

    def add(self, base, orbit):
        if base not in self.bodies:
            self.bodies[base] = Body(base)

        if orbit not in self.bodies:
            self.bodies[orbit] = Body(orbit)

        self.bodies[base].children.append(self.bodies[orbit])

    def check(self):
        self.check_sum = self.bodies["COM"].check()

    def path(self, target):
        target = self.bodies[target]
        return self.bodies["COM"].path(target)


if __name__ == "__main__":
    system = OrbitalMap()
    with open("input.txt") as f:
        for line in f:
            system.analyze(line.strip())
    system.check()
    my_path = system.path("YOU")
    san_path = system.path("SAN")
    distinct = []
    for body in my_path + san_path:
        if not (body in my_path and body in san_path):
            distinct.append(body)
    dist = len(distinct)
    print(f"Orbital Map Checksum: {system.check_sum}")
    print(f"Distance: {dist}")
