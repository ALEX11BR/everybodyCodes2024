#!/usr/bin/env python3

import re
from sys import stdin

NUM_ROT = 1048576000


if __name__ == "__main__":
    rot = input()
    input()
    text = [list(line) for line in stdin.read().splitlines()]

    rot_seq = [(0, 0)] * 8
    for i in range(2):
        rot_seq[i] = (-1, -1 + i)
        rot_seq[i + 2] = (-1 + i, 1)
        rot_seq[i + 4] = (1, 1 - i)
        rot_seq[i + 6] = (1 - i, -1)

    start = [[(i, j) for j in range(len(text[0]))] for i in range(len(text))]
    rot_i = 0
    for i in range(1, len(text) - 1):
        for j in range(1, len(text[i]) - 1):
            seq = rot_seq if rot[rot_i] == "R" else list(reversed(rot_seq))
            rot_i = (rot_i + 1) % len(rot)

            to_put = start[seq[-1][0] + i][seq[-1][1] + j]
            for k in range(len(seq)):
                aux = to_put
                to_put = start[seq[k][0] + i][seq[k][1] + j]
                start[seq[k][0] + i][seq[k][1] + j] = aux

    pre_rotations = [start]
    k = 2
    while k < NUM_ROT:
        new_rot = [[(i, j) for j in range(len(text[0]))]
                   for i in range(len(text))]

        for i in range(len(text)):
            for j in range(len(text[i])):
                dest1 = pre_rotations[-1][i][j]
                new_rot[i][j] = pre_rotations[-1][dest1[0]][dest1[1]]

        pre_rotations.append(new_rot)
        k <<= 1

    k = 0
    while (1 << k) < NUM_ROT:
        if (1 << k) & NUM_ROT:
            new_text = [["" for _ in range(len(text[0]))]
                        for _ in range(len(text))]

            for i in range(len(text)):
                for j in range(len(text[i])):
                    dest1 = pre_rotations[k][i][j]
                    dest2 = pre_rotations[k][dest1[0]][dest1[1]]
                    new_text[i][j] = text[dest1[0]][dest1[1]]
            text = new_text
        k += 1

    for line in text:
        ans = re.search(">([A-Z0-9]*)<", "".join(line))
        if ans:
            print(ans[1])
