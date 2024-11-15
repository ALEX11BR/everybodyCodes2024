#!/usr/bin/env python3

from math import inf
from sys import stdin

if __name__ == "__main__":
    numbers = [int(line) for line in stdin.read().splitlines()]
    bugs = [1, 3, 5, 10, 15, 16, 20, 24, 25, 30]
    limit = max(numbers) + 1
    dyn = [inf] * limit
    for b in bugs:
        dyn[b] = 1
    for i in range(2, limit):
        for b in bugs:
            if i - b > 0:
                dyn[i] = min(dyn[i], dyn[i - b] + 1)

    print(sum([dyn[i] for i in numbers]))
