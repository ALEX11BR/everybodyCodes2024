#!/usr/bin/env python3

from sys import stdin

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

    ans = " ".join([rolls[i][(nums[i] * 100) % len(rolls[i])]
                   for i in range(len(nums))])

    print(ans)
