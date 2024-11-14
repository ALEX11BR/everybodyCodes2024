#!/usr/bin/env python3

from collections import defaultdict
from sys import stdin

if __name__ == "__main__":
    mat = [[int(num) for num in line.split()]
           for line in stdin.read().splitlines()]
    rows = [[mat[i][j] for i in range(len(mat))] for j in range(len(mat[0]))]

    row = 0
    i = 0
    times = defaultdict(lambda: 0)

    while True:
        i += 1
        leader = rows[row].pop(0)
        newRow = (row + 1) % len(rows)
        pos = leader - 1
        if pos > len(rows[newRow]):
            pos = len(rows[newRow]) * 2 - pos
        rows[newRow].insert(pos, leader)
        row = newRow

        front = "".join([str(row[0]) for row in rows])
        times[front] += 1
        if times[front] == 2024:
            ans = int(front) * i
            break
    print(ans)
