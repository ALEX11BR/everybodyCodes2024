#!/usr/bin/env python3

if __name__ == "__main__":
    val = int(input())

    l = 1
    w = 1
    used = 1
    while used < 20240000:
        w += 2
        l = (l * val) % 1111
        used += l * w
    ans = w * (used - 20240000)
    print(ans)
