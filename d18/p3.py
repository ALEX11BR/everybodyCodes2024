#!/usr/bin/env python3

from collections import deque
from math import inf
from sys import stdin

if __name__ == "__main__":
    text = stdin.read().splitlines()

    ans = inf
    start = (1, 1)

    def neighbors(point: tuple[int, int]) -> list[tuple[int, int]]:
        ans = []
        for ii, jj in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            if point[0] + ii < 0 or point[1] + jj < 0 or point[0] + ii >= len(text) or point[1] + jj >= len(text[0]):
                continue
            if text[point[0] + ii][point[1] + jj] == "#":
                continue
            ans.append((point[0] + ii, point[1] + jj))
        return ans

    def ans_for(start: tuple[int, int]) -> int:
        l_ans = 0

        times = {start: 0}
        q = deque([start])
        while q:
            elem = q.popleft()
            if text[elem[0]][elem[1]] == "P":
                l_ans += times[elem]
            for i, j in neighbors(elem):
                if (i, j) in times:
                    continue
                q.append((i, j))
                times[(i, j)] = times[elem] + 1
        return l_ans

    bad = {start}
    q = deque([start])
    while q:
        elem = q.popleft()

        if text[elem[0]][elem[1]] != "P":
            l_ans = ans_for(elem)

            if l_ans > ans:
                continue

            ans = l_ans

        for p in neighbors(elem):
            if p in bad:
                continue
            bad.add(p)
            q.append(p)

    print(ans)
