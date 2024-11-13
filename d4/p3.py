#!/usr/bin/env python3

from math import inf

if __name__ == "__main__":
    nails = []
    try:
        while True:
            nails.append(int(input()))
    except EOFError:
        pass

    ans = inf

    for target in nails:
        ansT = 0
        for nail in nails:
            ansT += int(abs(target - nail))
        ans = min(ans, ansT)

    print(ans)
