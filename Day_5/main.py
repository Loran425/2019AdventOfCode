#!/usr/bin/env python
# Solution to the AOC2019 Challenge 9/10
# https://adventofcode.com/2019/day/5

from Utils import IntCodeMachine

data = [int(x) for x in open("input.txt").readline().strip().split(",")]
system = IntCodeMachine(data, [1])
system.execute()
