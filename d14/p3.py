#!/usr/bin/env python3

from collections import deque
from math import inf
from sys import stdin


def get_adjacent_points(point: tuple[int, int, int]) -> list[tuple[int, int, int]]:
    ans = []
    point = list(point)
    for i in range(3):
        for j in [-1, 1]:
            point[i] += j
            ans.append(tuple(point))
            point[i] -= j
    return ans


if __name__ == "__main__":
    trees = [line.split(",") for line in stdin.read().splitlines()]

    ans = inf
    points = set()
    main_points = set()
    leaves = set()
    for tree in trees:
        point = (0, 0, 0)
        for t in tree:
            for _ in range(int(t[1:])):
                point = list(point)
                if t[0] == "U":
                    point[0] += 1
                if t[0] == "D":
                    point[0] -= 1
                if t[0] == "R":
                    point[1] += 1
                if t[0] == "L":
                    point[1] -= 1
                if t[0] == "F":
                    point[2] += 1
                if t[0] == "B":
                    point[2] -= 1
                point = tuple(point)
                points.add(point)
                if point[1] == 0 and point[2] == 0:
                    main_points.add(point)
        leaves.add(point)

    costs = {node: 0 for node in main_points}
    for src in leaves:
        distances = {dest: inf for dest in points}
        distances[src] = 0
        q = deque()
        q.append(src)

        while q:
            elem = q.popleft()
            for neigh in get_adjacent_points(elem):
                if neigh in points and distances[neigh] == inf:
                    distances[neigh] = distances[elem] + 1
                    q.append(neigh)
        for node in main_points:
            costs[node] += distances[node]
    print(min(costs.values()))
