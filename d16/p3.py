#!/usr/bin/env python3

from collections import defaultdict
from functools import cache
from sys import stdin

ITERS = 256

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

    @cache
    def dyn(offset: int = 0, rolled: int = -1) -> tuple[int, int]:
        rolled += 1
        score = 0

        if rolled > 0:
            current_i = [(nums[i] * rolled + offset) % len(rolls[i])
                         for i in range(len(nums))]

            current_str = "".join([rolls[i][current_i[i]][j]
                                  for i in range(len(nums)) for j in [0, 2]])
            chars = defaultdict(lambda: 0)
            for char in current_str:
                chars[char] += 1

            for char, occ in chars.items():
                if occ >= 3:
                    score += occ - 2

            if rolled == ITERS:
                return score, score

        new_offsets = [offset + i for i in [-1, 0, 1]]
        partials = [dyn(new_offset, rolled) for new_offset in new_offsets]
        return (score + min([p[0] for p in partials])), (score + max([p[1] for p in partials]))

    ans = dyn()

    print(ans[1], ans[0])
