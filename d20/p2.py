#!/usr/bin/env python3

from collections import defaultdict, deque
from math import inf
from sys import stdin


def get_altitude_change(char: str) -> int:
    match char:
        case "-":
            return -2
        case "+":
            return 1
        case _:
            return -1


if __name__ == "__main__":
    text = stdin.read().splitlines()

    def neighbors_of(p: tuple[int, int], exclude_wall: bool = False) -> list[tuple[int]]:
        ans = []
        for k in range(4):
            point = list(p)
            point[k % 2] += (-1) ** (k // 2)

            if point[k % 2] < 0 or point[0] >= len(text) or point[1] >= len(text[0]):
                continue
            if text[point[0]][point[1]] == "#" and exclude_wall:
                continue
            ans.append(tuple(point))
        return ans

    def calc_dist(start: tuple[int, int], h=10000) -> int:
        ans = 1
        alti = defaultdict(lambda: -inf)
        for neigh in neighbors_of(start, False):
            alti[start, neigh, "ABCS"] = h

        while True:
            new_alti = defaultdict(lambda: -inf)
            for i in range(len(text)):
                for j in range(len(text[i])):
                    if text[i][j] == "#":
                        continue
                    for prev in neighbors_of((i, j)):
                        for k in reversed(range(4)):
                            new_alti[(i, j), prev, "ABCS"[k:]] = max([-inf] + [alti[prev, old, "ABCS"[k:]] +
                                                                               get_altitude_change(text[i][j]) for old in neighbors_of(prev) if old != (i, j)])
                            if text[i][j] == "ABCS"[k]:
                                new_alti[(i, j), prev, "ABCS"[
                                    (k+1):]] = max(new_alti[(i, j), prev, "ABCS"[(k+1):]], new_alti[(i, j), prev, "ABCS"[k:]])
            alti = new_alti

            maybe_alti = -inf
            for neigh in neighbors_of(start):
                if (start, neigh, "") in alti:
                    maybe_alti = max(maybe_alti, alti[start, neigh, ""])
            if maybe_alti >= h:
                return ans
            ans += 1

    points = {}
    for i in range(len(text)):
        for j in range(len(text[i])):
            if text[i][j] in "ABCS":
                points[text[i][j]] = (i, j)

    ans = calc_dist(points["S"])
    print(ans)
