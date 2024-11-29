#!/usr/bin/env python3

import re
from sys import stdin


def rotate(text: list[list[str]], rot: str) -> str:
    rot_seq = [(0, 0)] * 8
    for i in range(2):
        rot_seq[i] = (-1, -1 + i)
        rot_seq[i + 2] = (-1 + i, 1)
        rot_seq[i + 4] = (1, 1 - i)
        rot_seq[i + 6] = (1 - i, -1)

    rot_i = 0

    while True:
        for i in range(1, len(text) - 1):
            for j in range(1, len(text[i]) - 1):
                seq = rot_seq if rot[rot_i] == "R" else list(reversed(rot_seq))
                rot_i = (rot_i + 1) % len(rot)

                to_put = text[seq[-1][0] + i][seq[-1][1] + j]
                for k in range(len(seq)):
                    aux = to_put
                    to_put = text[seq[k][0] + i][seq[k][1] + j]
                    text[seq[k][0] + i][seq[k][1] + j] = aux

        for line in text:
            ans = re.search(">(.*)<", "".join(line))
            if ans:
                return ans[1]


if __name__ == "__main__":
    rot = input()
    input()
    text = [list(line) for line in stdin.read().splitlines()]

    print(rotate(text, rot))
