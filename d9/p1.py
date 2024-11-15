#!/usr/bin/env python3

from math import inf
from sys import stdin

if __name__ == "__main__":
    numbers = [int(line) for line in stdin.read().splitlines()]
    limit = max(numbers) + 1
    dyn = [inf] * limit
    dyn[1] = 1
    dyn[3] = 1
    dyn[5] = 1
    dyn[10] = 1
    for i in range(2, limit):
        if i - 1 > 0:
            dyn[i] = min(dyn[i], dyn[i - 1] + 1)
        if i - 3 > 0:
            dyn[i] = min(dyn[i], dyn[i - 3] + 1)
        if i - 5 > 0:
            dyn[i] = min(dyn[i], dyn[i - 5] + 1)
        if i - 10 > 0:
            dyn[i] = min(dyn[i], dyn[i - 10] + 1)

    print(sum([dyn[i] for i in numbers]))
