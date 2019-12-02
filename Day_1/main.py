#!/usr/bin/env python
# Solution to the AOC2019 Challenge 1/2
# https://adventofcode.com/2019/day/1
from enum import Enum


class FuelCalc(Enum):
    SIMPLE = 0
    COMPLEX = 1


def basic_fuel_cost(mass: int) -> int:
    return mass // 3 - 2


def complex_fuel_cost(mass: int) -> int:
    fuel = basic_fuel_cost(mass)
    if fuel <= 0:
        return 0
    else:
        return fuel + complex_fuel_cost(fuel)


def fuel_cost(mass: int, method: int = FuelCalc.SIMPLE):
    if method == FuelCalc.SIMPLE:
        return basic_fuel_cost(mass)
    elif method == FuelCalc.COMPLEX:
        return complex_fuel_cost(mass)
    else:
        raise ValueError("Unable to determine calculation cost")


if __name__ == "__main__":
    with open("input.txt") as f:
        simple_fuel_total = 0
        complex_fuel_total = 0
        for line in f:
            mass = int(line)
            simple_fuel_total += basic_fuel_cost(mass)
            complex_fuel_total += complex_fuel_cost(mass)
        print(f"Simple Fuel: {simple_fuel_total}")
        print(f"Complex Fuel: {complex_fuel_total}")
