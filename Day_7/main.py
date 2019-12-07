#!/usr/bin/env python
# Solution to the AOC2019 Challenge 13/14
# https://adventofcode.com/2019/day/7

import itertools
from Utils import IntCodeMachine


data = [int(x) for x in open("input.txt").readline().strip().split(",")]
# Challenge 13
max_output = (0, 0)
for pattern in itertools.permutations(range(5)):
    machines = list()
    for num in range(5):
        machines.append(IntCodeMachine(data, [pattern[num]], []))

    buffer = [0]

    for machine in machines:
        machine.input_stream += buffer
        machine.execute()
        buffer = [machine.output_stream.pop(0)]

    if buffer[0] > max_output[1]:
        max_output = (pattern, buffer[0])
print("[Single Cycle]")
print(f"Configuration: {max_output[0]}")
print(f"Thrust: {max_output[1]}")

# Challenge 14
max_output = (0, 0)
for pattern in itertools.permutations(range(5, 10)):
    machines = list()
    for num in range(5):
        machines.append(IntCodeMachine(data, [pattern[num]], []))

    buffer = [0]
    cycle_done = False
    while not cycle_done:
        for machine in machines:
            machine.input_stream += buffer
            machine.execute()
            if machine.output_stream:
                buffer = [machine.output_stream.pop(0)]
            else:
                cycle_done = True

        if buffer[0] > max_output[1]:
            max_output = (pattern, buffer[0])

print("[Feedback Cycle]")
print(f"Configuration: {max_output[0]}")
print(f"Thrust: {max_output[1]}")
