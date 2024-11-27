#!/usr/bin/env python3

from collections import deque
from sys import stdin

if __name__ == "__main__":
    text = stdin.read().splitlines()

    ans = 0
    start = (1, 0)

    def neighbors(point: tuple[int, int]) -> list[tuple[int, int]]:
        ans = []
        for ii, jj in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            if point[0] + ii < 0 or point[1] + jj < 0 or point[0] + ii >= len(text) or point[1] + jj >= len(text[0]):
                continue
            if text[point[0] + ii][point[1] + jj] == "#":
                continue
            ans.append((point[0] + ii, point[1] + jj))
        return ans

    times = {start: 0}
    q = deque([start])
    while q:
        elem = q.popleft()
        if text[elem[0]][elem[1]] == "P":
            ans = times[elem]
        for i, j in neighbors(elem):
            if (i, j) in times:
                continue
            q.append((i, j))
            times[(i, j)] = times[elem] + 1

    print(ans)
