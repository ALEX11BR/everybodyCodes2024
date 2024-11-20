#!/usr/bin/env python3

import heapq
from math import inf
from sys import stdin


def height_diff(a: int, b: int) -> int:
    return min(abs(a - b), abs(a - b + 10), abs(a - b - 10))


if __name__ == "__main__":
    text = stdin.read().splitlines()

    ans = 0

    for i in range(len(text)):
        for j in range(len(text[i])):
            if text[i][j] == "S":
                start = (i, j)
            if text[i][j] == "E":
                end = (i, j)

    q = []
    heapq.heappush(q, (0, start))
    dist_to = [[inf] * len(text[0]) for _ in range(len(text))]

    def get_h(i: int, j: int) -> int:
        if i < 0 or j < 0 or i >= len(text) or j >= len(text[0]) or text[i][j] == "#":
            return -1
        if text[i][j] in "SE":
            return 0
        return int(text[i][j])

    while q:
        d, (i, j) = heapq.heappop(q)
        if dist_to[i][j] < inf:
            continue
        dist_to[i][j] = d

        for ii, jj in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
            h = get_h(i + ii, j + jj)
            if h == -1:
                continue
            new_dist = dist_to[i][j] + height_diff(h, get_h(i, j)) + 1
            if new_dist < dist_to[i + ii][j + jj]:
                heapq.heappush(q, (new_dist, (i + ii, j + jj)))

    ans = dist_to[end[0]][end[1]]
    print(ans)
