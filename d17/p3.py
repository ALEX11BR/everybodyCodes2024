#!/usr/bin/env python3

from math import inf
from sys import stdin


def dist(a: tuple[int, int], b: tuple[int, int]) -> int:
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


if __name__ == "__main__":
    text = stdin.read().splitlines()

    stars = set()
    stars_in_all = set()
    sets = []
    for i in range(len(text)):
        for j in range(len(text[0])):
            if text[i][j] == "*":
                stars.add((i, j))

    for start_star in stars:
        if start_star in stars_in_all:
            continue
        stars_in = set([start_star])

        ans_sum = 0
        while True:
            next_star = None
            next_len = inf
            for src in stars_in:
                for dest in stars.difference(stars_in_all).difference(stars_in):
                    if next_len > dist(src, dest):
                        next_len = dist(src, dest)
                        next_star = dest
            if next_len >= 6:
                break
            stars_in.add(next_star)
            ans_sum += next_len

        stars_in_all.update(stars_in)
        sets.append(len(stars_in) + ans_sum)

    sets.sort(reverse=True)
    print(sets[0] * sets[1] * sets[2])
