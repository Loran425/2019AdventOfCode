#!/usr/bin/env python
# Solution to the AOC2019 Challenge 9/10
# https://adventofcode.com/2019/day/5
from enum import Enum


class MODE(Enum):
    Position = 0
    Immediate = 1


class OPCODE(Enum):
    Addition = 1
    Multiplication = 2
    Input = 3
    Output = 4
    JumpIfTrue = 5
    JumpIfFalse = 6
    LessThan = 7
    Equal = 8
    Exit = 99


class IntCodeMachine:
    def __init__(self, program):
        self.program = program
        self.pointer = 0
        self.ops = {
            OPCODE.Addition: self.add,
            OPCODE.Multiplication: self.mul,
            OPCODE.Input: self.input,
            OPCODE.Output: self.output,
            OPCODE.JumpIfTrue: self.jump_if_true,
            OPCODE.JumpIfFalse: self.jump_if_false,
            OPCODE.LessThan: self.less_than,
            OPCODE.Equal: self.equal,
        }

    def __len__(self):
        return len(self.program)

    def __getitem__(self, key):
        return self.program[key]

    def __setitem__(self, key, value):
        self.program[key] = value

    def execute(self):
        while True:
            op, params = self.parse(self[self.pointer])
            if op == OPCODE.Exit:
                return self.program
            else:
                self.ops[op](params)

    def parse(self, code: int):
        if code < 99:
            op_code = code
            params = []
        else:
            op_code = code - code // 100 * 100

            # Extract raw parameters by removing the last 2 digits (the op code)
            params = [MODE(int(x)) for x in str(code // 100)]
            # params are stored in reverse order in program
            params.reverse()

        # ensure we have the enough parameter flags
        # max needed is 3, other functions will ignore extra values
        # empty values are 0's (position access mode)
        while len(params) < 3:
            params.append(MODE.Position)

        # Change from integer op_code to enum OPCODE
        try:
            op_code = OPCODE(op_code)
        except ValueError:
            raise ValueError(f"Unknown OPCODE: {op_code} at position {self.pointer}")

        return op_code, params

    def read(self, offset, mode: MODE):
        if mode == MODE.Position:
            return self[self[self.pointer + offset]]
        elif mode == MODE.Immediate:
            return self[self.pointer + offset]
        else:
            raise ValueError("Invalid Access Mode")

    def write(self, offset, value):
        self[self[self.pointer + offset]] = value

    def add(self, params):
        a = self.read(1, params[0])
        b = self.read(2, params[1])
        self.write(3, a + b)
        self.pointer += 4

    def mul(self, params):
        a = self.read(1, params[0])
        b = self.read(2, params[1])
        self.write(3, a * b)
        self.pointer += 4

    def input(self, params):
        var = input("Input:")

        try:
            var = int(var)
        except ValueError:
            print("Invalid input. System can only accept integers")
            exit()

        self.write(1, var)
        self.pointer += 2

    def output(self, params):
        output = self.read(1, params[0])
        print(f"Program Output:{output}")
        self.pointer += 2

    def jump_if_true(self, params):
        if self.read(1, params[0]):
            self.pointer = self.read(2, params[1])
        else:
            self.pointer += 3

    def jump_if_false(self, params):
        if not self.read(1, params[0]):
            self.pointer = self.read(2, params[1])
        else:
            self.pointer += 3

    def less_than(self, params):
        if self.read(1, params[0]) < self.read(2, params[1]):
            self.write(3, 1)
        else:
            self.write(3, 0)
        self.pointer += 4

    def equal(self, params):
        if self.read(1, params[0]) == self.read(2, params[1]):
            self.write(3, 1)
        else:
            self.write(3, 0)
        self.pointer += 4


if __name__ == "__main__":
    data = [int(x) for x in open("input.txt").readline().strip().split(",")]
    system = IntCodeMachine(data)
    system.execute()
