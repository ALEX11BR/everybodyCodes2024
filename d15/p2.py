#!/usr/bin/env python3

from collections import deque
from math import inf
from sys import stdin


def bfs(world: list[str], src: tuple[int, int], to_collect: set[str]) -> int:
    visited = set()

    q = deque([(src, 0, set())])
    while q:
        elem, dist, collected = q.popleft()
        if (elem, frozenset(collected)) in visited:
            continue
        if elem == src and collected == to_collect:
            return dist
        visited.add((elem, frozenset(collected)))

        for ii, jj in [(1, 0), (-1, 0), (0, -1), (0, 1)]:
            if elem[0] + ii < 0 or elem[0] + ii >= len(world) or elem[1] + jj < 0 or elem[1] + jj >= len(world[0]):
                continue
            if world[elem[0] + ii][elem[1] + jj] in "#~":
                continue

            if world[elem[0] + ii][elem[1] + jj].isalpha():
                new_collected = collected | set(
                    [world[elem[0] + ii][elem[1] + jj]])
            else:
                new_collected = collected

            if ((elem[0] + ii, elem[1] + jj), frozenset(new_collected)) in visited:
                continue
            q.append(((elem[0] + ii, elem[1] + jj), dist + 1, new_collected))

    return inf


if __name__ == "__main__":
    world = stdin.read().splitlines()

    herbs = set()
    start = (0, 0)
    for i in range(len(world)):
        for j in range(len(world[i])):
            if world[i][j].isalpha():
                herbs.add(world[i][j])
            if world[i][j] == "." and i == 0:
                start = (i, j)

    ans = bfs(world, start, herbs)

    print(ans)
