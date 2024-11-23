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

    seg_world = [[line[(i * len(world[0]) // 3):((i + 1) * len(world[0]) // 3)]
                  for line in world] for i in range(3)]

    ans = 0

    herbs = set()
    start = (len(world) - 2, len(world[0]) // 3 - 1)
    for i in range(len(seg_world[0])):
        for j in range(len(seg_world[0][i])):
            if seg_world[0][i][j].isalpha():
                herbs.add(seg_world[0][i][j])
    ans += bfs(seg_world[0], start, herbs)

    herbs = set()
    start = (0, 0)
    seg_world[1][len(world) - 2] = "Z" + \
        seg_world[1][len(world) - 2][1:-1] + "Y"
    for i in range(len(seg_world[1])):
        for j in range(len(seg_world[1][i])):
            if seg_world[1][i][j].isalpha():
                herbs.add(seg_world[1][i][j])
            if seg_world[1][i][j] == "." and i == 0:
                start = (i, j)
    ans += bfs(seg_world[1], start, herbs)

    herbs = set()
    start = (len(world) - 2, 0)
    for i in range(len(seg_world[2])):
        for j in range(len(seg_world[2][i])):
            if seg_world[2][i][j].isalpha():
                herbs.add(seg_world[2][i][j])
    ans += bfs(seg_world[2], start, herbs)

    ans += 4

    print(ans)
