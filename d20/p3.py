#!/usr/bin/env python3

from sys import stdin


def height_diff(char: str) -> int:
    if char == "+":
        return 1
    return -1


if __name__ == "__main__":
    text = stdin.read().splitlines()

    h = 384400 - 3
    column = 31

    ans = 0
    while h > 0:
        ans += 1
        h += height_diff(text[ans % len(text)][column])

    print(ans)
