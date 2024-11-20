#!/usr/bin/env python3

from sys import stdin

if __name__ == "__main__":
    text = stdin.readlines()

    ans = 0
    targets = []
    for i in range(len(text)):
        for j in range(len(text[i])):
            if text[i][j] in "TH":
                targets.append((i, j, 1 if text[i][j] == "T" else 2))
    correction = len(text) - 5

    for t_i, t_j, t_pow in targets:
        ans_let = (t_j + correction - t_i) % 3 or 3
        ans_pow = (t_j + correction - t_i + 2) // 3

        ans += ans_pow * ans_let * t_pow
    print(ans)
