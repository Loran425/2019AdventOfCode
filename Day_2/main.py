#!/usr/bin/env python
# Solution to the AOC2019 Challenge 3/4
# https://adventofcode.com/2019/day/2
import copy
from typing import List
from enum import Enum


program = List[int]


class OPCODE(Enum):
    Addition = 1
    Multiplication = 2
    Return = 99


def intcode(data: program):
    pointer = 0

    while True:
        op = data[pointer]

        if op == OPCODE.Addition.value:
            in_1 = data[pointer + 1]
            in_2 = data[pointer + 2]
            out = data[pointer + 3]
            data[out] = data[in_1] + data[in_2]
            pointer += 4
        elif op == OPCODE.Multiplication.value:
            in_1 = data[pointer + 1]
            in_2 = data[pointer + 2]
            out = data[pointer + 3]
            data[out] = data[in_1] * data[in_2]
            pointer += 4
        elif op == OPCODE.Return.value:
            return data
        else:
            raise ValueError(f"Unknown OPCODE: {op} at position {pointer}")


if __name__ == "__main__":
    data = [int(x) for x in open("input.txt").readline().strip().split(",")]
    backup = copy.deepcopy(data)
    data[1] = 12
    data[2] = 2
    output = intcode(data)
    print(f"Error state 1202 has {output[0]} at position 0")

    for x in range(100):
        for y in range(100):
            data = copy.deepcopy(backup)
            data[1] = x
            data[2] = y
            temp = intcode(data)
            if temp[0] == 19690720:
                print(f"IntCode Program outputs 19690720 with noun [{x}], verb[{y}]")
