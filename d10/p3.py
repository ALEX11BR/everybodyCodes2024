#!/usr/bin/env python3

from sys import stdin

if __name__ == "__main__":
    world = [[c for c in line] for line in stdin.read().splitlines()]

    res = 0
    solved = set()
    isDone = False
    while not isDone:
        isDone = True
        for i0 in range(0, len(world) - 2, 6):
            for j0 in range(0, len(world[0]) - 2, 6):
                if (i0, j0) in solved:
                    continue
                ans = ["?"] * 16
                allSymbols = set()
                placedSymbols = set()
                for i in range(2, 6):
                    for j in range(2, 6):
                        onLines = set(
                            world[i0 + i][j0:j0+2] + world[i0 + i][j0+6:j0+8])
                        if "?" in onLines:
                            onLines.remove("?")
                        onColumns = set([world[x][j0 + j]
                                        for x in [i0, i0 + 1, i0 + 6, i0 + 7] if world[x][j0 + j] != "?"])
                        allSymbols.update(onLines)
                        allSymbols.update(onColumns)
                        common = list(onLines.intersection(onColumns))
                        if len(common) > 0:
                            ans[4 * (i - 2) + (j - 2)] = common[0]
                            placedSymbols.add(common[0])
                todoSymbols = allSymbols - placedSymbols
                isPossible = True
                while isPossible:
                    isPossible = False
                    for i in range(2, 6):
                        for j in range(2, 6):
                            onLines = set(
                                world[i0 + i][j0:j0+2] + world[i0 + i][j0+6:j0+8])
                            if "?" in onLines:
                                onLines.remove("?")
                            onColumns = set([world[x][j0 + j]
                                            for x in [i0, i0 + 1, i0 + 6, i0 + 7] if world[x][j0 + j] != "?"])
                            possible = list(
                                (onLines ^ onColumns) & todoSymbols)
                            if len(possible) == 1 and ans[4 * (i - 2) + (j - 2)] == "?":
                                ans[4 * (i - 2) + (j - 2)] = possible[0]
                                todoSymbols.discard(possible[0])
                                isPossible = True
                                for (ii, jj) in [(i1, j0 + j) for i1 in [i0, i0 + 1, i0 + 6, i0 + 7]] + [(i0 + i, j1) for j1 in [j0, j0 + 1, j0 + 6, j0 + 7]]:
                                    if world[ii][jj] == "?":
                                        world[ii][jj] = possible[0]
                if "?" in ans:
                    continue
                isDone = False
                solved.add((i0, j0))
                for i in range(len(ans)):
                    res += (i + 1) * (ord(ans[i]) - ord("A") + 1)
    print(res)
