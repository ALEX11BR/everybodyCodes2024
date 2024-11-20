#!/usr/bin/env python3

from math import inf
from sys import stdin

if __name__ == "__main__":
    ans = 0

    for line in stdin:
        coords = [int(c) for c in line.strip().split(" ")]

        x_clash = coords[0] // 2
        this_ans = inf
        for i in range(3):
            y_clash = coords[1] - (coords[0] - x_clash) - i

            if x_clash < y_clash:
                continue
            if x_clash == y_clash:
                this_ans = min(this_ans, y_clash * (i + 1))
            elif x_clash <= y_clash * 2:
                this_ans = min(this_ans, y_clash * (i + 1))
            else:
                if (y_clash + x_clash) % 3 != 0:
                    continue
                this_ans = min(this_ans, (y_clash + x_clash) // 3 * (i + 1))
        ans += this_ans

    print(ans)
