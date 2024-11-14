#!/usr/bin/env python3

from collections import deque
from sys import stdin

def bfs(tree: dict[str, list[str]]) -> list[str]:
    q = deque()
    q.append(("RR", "R"))
    pathsToFruits = []

    while len(q) > 0:
        node, path = q.popleft()
        if node == "@":
            pathsToFruits.append(path)
            continue
        try:
            for neigh in tree[node]:
                if neigh in ["BUG", "ANT"]:
                    continue
                q.append((neigh, path + neigh[0]))
        except KeyError:
            pass

    return pathsToFruits

if __name__ == "__main__":
    tree = {}
    for line in stdin.read().splitlines():
        elems = line.split(":")
        tree[elems[0]] = elems[1].split(",")

    paths = bfs(tree)
    sizes = set()
    goodSizes = set()
    for path in paths:
        if len(path) in sizes:
            try:
                goodSizes.remove(len(path))
            except KeyError:
                pass
        else:
            goodSizes.add(len(path))
            sizes.add(len(path))
    for path in paths:
        if len(path) in goodSizes:
            ans = path
    print(ans)
