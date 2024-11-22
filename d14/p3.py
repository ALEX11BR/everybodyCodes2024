#!/usr/bin/env python3

# TODO
 
from sys import stdin

if __name__ == "__main__":
    trees = [line.split(",") for line in stdin.read().splitlines()]

    ans = 0
    points = set()
    main_points = set()
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

    ans = len(points)
    print(ans)
