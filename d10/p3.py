#!/usr/bin/env python3

# TODO

from sys import stdin

if __name__ == "__main__":
    worldsStr = stdin.read().splitlines()
    worlds = []
    for yStart in range(0, len(worldsStr) - 2, 7):
        for xStart in range(0, len(worldsStr[0]) - 2, 7):
            worlds.append([worldsStr[i][xStart:xStart+8]
                          for i in range(yStart, yStart + 8)])

    res = 0
    for world in worlds:
        ans = ""
        for i in range(2, len(world) - 2):
            for j in range(2, len(world[i]) - 2):
                onLines = set(world[i][0:2] + world[i][-2:])
                if "?" in onLines:
                    onLines.remove("?")
                onColumns = set([world[x][j]
                                for x in [0, 1, -2, -1] if world[x][j] != "?"])
                common = list(onLines.intersection(onColumns))
                if len(common) > 0:
                    ans += common[0]
        for i in range(len(ans)):
            res += (i + 1) * (ord(ans[i]) - ord("A") + 1)
    print(res)
