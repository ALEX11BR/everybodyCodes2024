#!/usr/bin/env python3

from sys import stdin


def rows2str(rows: list[list[int]]) -> str:
    return "-".join([".".join([str(elem) for elem in row]) for row in rows])


if __name__ == "__main__":
    mat = [[int(num) for num in line.split()]
           for line in stdin.read().splitlines()]
    rows = [[mat[i][j] for i in range(len(mat))] for j in range(len(mat[0]))]

    row = 0
    i = 0
    states = set()

    while True:
        i += 1
        front = "".join([str(row[0]) for row in rows])
        rowStr = rows2str(rows)
        if (front, rowStr) in states:
            ans = max(states)[0]
            break
        states.add((front, rowStr))

        leader = rows[row].pop(0)
        newRow = (row + 1) % len(rows)
        pos = (leader - 1) % (2 * len(rows[newRow]))
        if pos > len(rows[newRow]):
            pos = len(rows[newRow]) * 2 - pos
        rows[newRow].insert(pos, leader)
        row = newRow
    print(ans)
