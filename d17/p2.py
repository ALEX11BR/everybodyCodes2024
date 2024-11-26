#!/usr/bin/env python3

from math import inf
from sys import stdin


def dist(a: tuple[int, int], b: tuple[int, int]) -> int:
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


if __name__ == "__main__":
    text = stdin.read().splitlines()

    stars = set()
    stars_in = set()
    for i in range(len(text)):
        for j in range(len(text[0])):
            if text[i][j] == "*":
                stars.add((i, j))
                if not stars_in:
                    stars_in.add((i, j))

    ans = len(stars)
    while len(stars) != len(stars_in):
        next_star = None
        next_len = inf
        for src in stars_in:
            for dest in stars.difference(stars_in):
                if next_len > dist(src, dest):
                    next_len = dist(src, dest)
                    next_star = dest
        stars_in.add(next_star)
        ans += next_len

    print(ans)
