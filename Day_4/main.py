#!/usr/bin/env python
# Solution to the AOC2019 Challenge 7/8
# https://adventofcode.com/2019/day/4
import typing
from tqdm import tqdm

digit_list = typing.List[int]


def password_check(password: str, strict: bool = False) -> bool:
    digits = [int(x) for x in password]
    valid = ascending_check(digits) and double_digit_check(digits, strict=strict)
    return valid


def ascending_check(digits: digit_list) -> bool:
    temp = 0
    for digit in digits:
        if digit < temp:
            return False
        else:
            temp = digit
    return True


def double_digit_check(digits: digit_list, strict: bool = False) -> bool:
    prev = None
    if not strict:
        for digit in digits:
            if digit == prev:
                return True
            else:
                prev = digit
        return False
    else:
        repeated = []
        for digit in digits:
            if digit == prev:
                repeated[-1].append(digit)
            else:
                repeated.append([digit])
            prev = digit
        return any([len(x) == 2 for x in repeated])


if __name__ == "__main__":
    possible_passwords = [0, 0]
    INPUT = range(357253, 892942)
    for pw in tqdm(INPUT):
        if password_check(str(pw)):
            possible_passwords[0] += 1
    for pw in tqdm(INPUT):
        if password_check(str(pw), strict=True):
            possible_passwords[1] += 1
    print(f"Relaxed Possible Passwords: {possible_passwords[0]}")
    print(f" Strict Possible Passwords: {possible_passwords[1]}")
