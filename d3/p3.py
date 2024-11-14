#!/usr/bin/env python3

import sys


class World:
    def __init__(self, world: list[str]) -> None:
        self.world = world

    def inBounds(self, y: int, x: int) -> bool:
        return y >= 0 and x >= 0 and y < len(self.world) and x < len(self.world[0])

    def isSurface(self, y: int, x: int) -> bool:
        return (not self.inBounds(y, x)) or self.world[y][x] == "."

    def getSlope(self, y: int, x: int) -> int:
        if self.world[y][x] == ".":
            return 0
        l = 1
        while True:
            for k in range(2 * l):
                if self.isSurface(y - l, x - (l - k)):
                    return l
                if self.isSurface(y - (l - k), x + l):
                    return l
                if self.isSurface(y + l, x + (l - k)):
                    return l
                if self.isSurface(y + (l - k), x - l):
                    return l
            l += 1


if __name__ == "__main__":
    world = World(sys.stdin.read().splitlines())

    ans = 0
    for y in range(len(world.world)):
        for x in range(len(world.world[0])):
            ans += world.getSlope(y, x)

    print(ans)
