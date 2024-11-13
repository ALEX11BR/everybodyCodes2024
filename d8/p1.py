#!/usr/bin/env python3

if __name__ == "__main__":
    val = int(input())

    w = 1
    s = 1
    while s < val:
        w += 2
        s += w
    ans = (s - val) * w
    print(ans)
