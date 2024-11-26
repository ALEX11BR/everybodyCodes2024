#!/usr/bin/env python3

from collections import defaultdict
from math import gcd, lcm
from sys import stdin

ITERS = 202420242024

if __name__ == "__main__":
    nums = list(map(int, input().split(",")))
    input()

    text = stdin.read().splitlines()
    rolls = [[] for _ in nums]

    for i in range(len(nums)):
        for line in text:
            if len(line) < 4 * i + 2 or line[i*4] == " ":
                continue
            item = line[(i*4):(i*4 + 3)]
            rolls[i].append(item)

    ans = 0

    repeats_after = [len(rolls[i]) // gcd(nums[i], len(rolls[i]))
                     for i in range(len(nums))]
    cycle_len = lcm(*repeats_after)

    cost_add = [0]
    cost = 0
    current_i = [0] * len(nums)
    for _ in range(cycle_len):
        current_i = [(nums[i] + current_i[i]) % len(rolls[i])
                     for i in range(len(nums))]
        current_str = "".join([rolls[i][current_i[i]][j]
                              for i in range(len(nums)) for j in [0, 2]])
        chars = defaultdict(lambda: 0)
        for char in current_str:
            chars[char] += 1
        score = 0
        for char, occ in chars.items():
            if occ >= 3:
                score += occ - 2
        cost_add.append(cost_add[-1] + score)

    ans = cost_add[-1] * (ITERS // cycle_len) + cost_add[ITERS % cycle_len]

    print(ans)
