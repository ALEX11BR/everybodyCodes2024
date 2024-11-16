#!/usr/bin/env python3

from sys import stdin

if __name__ == "__main__":
    world = stdin.read().splitlines()

    ans = ""
    for i in range(2, len(world) - 2):
        for j in range(2, len(world[i]) - 2):
            onLines = set(world[i][0:2] + world[i][-2:])
            onColumns = set([world[x][j] for x in [0, 1, -2, -1]])
            ans += list(onLines.intersection(onColumns))[0]
    print(ans)
