#!/usr/bin/env python3

from sys import stdin


def calc(termites: dict[str, list[str]], termite: str) -> int:
    cache = {t: 0 for t in termites}
    cache[termite] = 1
    for _ in range(20):
        newCache = {t: 0 for t in termites}
        for t in cache:
            for newElement in termites[t]:
                newCache[newElement] += cache[t]
        cache = newCache
    return sum(cache.values())


if __name__ == "__main__":
    termites = {}
    for line in stdin.read().splitlines():
        l1 = line.split(":")
        termites[l1[0]] = l1[1].split(",")

    anses = [calc(termites, t) for t in termites]

    print(max(anses) - min(anses))
