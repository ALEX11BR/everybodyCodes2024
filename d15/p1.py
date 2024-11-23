#!/usr/bin/env python3

from collections import deque
from math import inf
from sys import stdin


def bfs(world: list[str], src: tuple[int, int]) -> list[list[int]]:
    ans = [[inf for _ in range(len(world[0]))] for _ in range(len(world))]
    ans[src[0]][src[1]] = 0

    q = deque([src])
    while q:
        elem = q.popleft()
        for ii, jj in [(1, 0), (-1, 0), (0, -1), (0, 1)]:
            if elem[0] + ii < 0 or elem[0] + ii >= len(world) or elem[1] + jj < 0 or elem[1] + jj >= len(world[0]):
                continue
            if world[elem[0] + ii][elem[1] + jj] == "#":
                continue
            if ans[elem[0] + ii][elem[1] + jj] != inf:
                continue
            ans[elem[0] + ii][elem[1] + jj] = ans[elem[0]][elem[1]] + 1
            q.append((elem[0] + ii, elem[1] + jj))

    return ans


if __name__ == "__main__":
    world = stdin.read().splitlines()

    herbs = []
    start = (0, 0)
    for i in range(len(world)):
        for j in range(len(world[i])):
            if world[i][j] == "H":
                herbs.append((i, j))
            if world[i][j] == "." and i == 0:
                start = (i, j)

    ans = inf
    src_dist = bfs(world, start)
    for h in herbs:
        back_dist = bfs(world, h)

        ans = min(ans, src_dist[h[0]][h[1]] + back_dist[start[0]][start[1]])

    print(ans)
