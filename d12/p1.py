#!/usr/bin/env python3

from sys import stdin

if __name__ == "__main__":
    text = stdin.readlines()

    ans = 0
    targets = []
    for i in range(len(text)):
        for j in range(len(text[i])):
            if text[i][j] == "T":
                targets.append((i, j))

    for t_i, t_j in targets:
        ans_let = (t_j - t_i) % 3 or 3
        ans_pow = (t_j - t_i + 2) // 3

        ans += ans_pow * ans_let
    print(ans)
