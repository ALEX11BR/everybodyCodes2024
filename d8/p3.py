#!/usr/bin/env python3

if __name__ == "__main__":
    val = int(input())

    columns = [1]
    l = 1
    w = 1
    used = 1
    while used < 202400000:
        w += 2
        l = (l * val) % 10 + 10
        columns = [x + l for x in columns] + [l]
        used += l * w
    for i in range(1, len(columns) - 1):
        used -= ((val * w * columns[i]) % 10) * 2
    used -= (val * w * columns[0]) % 10
    ans = (used - 202400000)
    print(ans)
