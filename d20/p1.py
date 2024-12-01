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

    def neighbors_of(p: tuple[int, int]) -> list[tuple[int]]:
        ans = []
        for k in range(4):
            point = list(p)
            point[k % 2] += (-1) ** (k // 2)

            if point[k % 2] < 0 or point[0] >= len(text) or point[1] >= len(text[0]):
                continue
            if text[point[0]][point[1]] == "#":
                continue
            ans.append(tuple(point))
        return ans

    dist = defaultdict(lambda: -inf)
    for i in range(len(text)):
        for j in range(len(text[i])):
            if text[i][j] == "S":
                start = (i, j)
                for neigh in neighbors_of(start):
                    dist[start, neigh] = 1000

    for _ in range(100):
        new_dist = defaultdict(lambda: -inf)
        for i in range(len(text)):
            for j in range(len(text[i])):
                for prev in neighbors_of((i, j)):
                    new_dist[(i, j), prev] = max([-inf] + [dist[prev, old] + get_altitude_change(
                        text[i][j]) for old in neighbors_of(prev) if old != (i, j)])
        dist = new_dist

    ans = max(dist.values())
    print(ans)
