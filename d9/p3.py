#!/usr/bin/env python3

from math import inf
from sys import stdin

if __name__ == "__main__":
    numbers = [int(line) for line in stdin.read().splitlines()]
    bugs = [1, 3, 5, 10, 15, 16, 20, 24, 25, 30, 37, 38, 49, 50, 74, 75, 100, 101]
    limit = max(numbers) + 1
    dyn = [inf] * limit
    for b in bugs:
        dyn[b] = 1
    for i in range(2, limit):
        for b in bugs:
            if i - b > 0:
                dyn[i] = min(dyn[i], dyn[i - b] + 1)
    ans = 0
    for num in numbers:
        localAns = inf
        lowerBound = num // 2 - 50 + num % 2
        for i in range(lowerBound, num // 2 + 1):
            localAns = min(localAns, dyn[i] + dyn[num - i])
        ans += localAns
    print(ans)
