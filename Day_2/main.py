#!/usr/bin/env python
# Solution to the AOC2019 Challenge 3/4
# https://adventofcode.com/2019/day/2
import copy
from Utils import IntCodeMachine

data = [int(x) for x in open("input.txt").readline().strip().split(",")]
system = IntCodeMachine(copy.deepcopy(data))
system[1] = 12
system[2] = 2
output = system.execute()
print(f"Error state 1202 has {output[0]} at position 0")

for x in range(100):
    for y in range(100):
        system = IntCodeMachine(copy.deepcopy(data))
        system[1] = x
        system[2] = y
        temp = system.execute()
        if temp[0] == 19690720:
            print(f"IntCode Program outputs 19690720 with noun [{x}], verb[{y}]")
