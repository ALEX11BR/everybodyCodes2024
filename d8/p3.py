#!/usr/bin/env python3

#TODO

if __name__ == "__main__":
    val = int(input())

    columns = [1]
    l = 1
    ls = [1]
    lrepeat = -1
    w = 1
    used = 1
    while used < 202400000000:
        w += 2
        l = (l * val) % 10 + 10
        if lrepeat == -1:
            if l in ls:
                lrepeat = ls.index(l)
            else:
                ls.append(l)
        columns = [l] + [x + l for x in columns] + [l]
        used += l * w
    for i in range(1, len(columns) - 1):
        used -= (val * w * columns[i]) % 10
    ans = (used - 202400000000)
    print(ans)
