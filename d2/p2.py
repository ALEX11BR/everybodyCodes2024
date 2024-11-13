#!/usr/bin/env python3

import sys

if __name__ == "__main__":
    init = input()
    input()
    text = sys.stdin.read()

    words = init.split(":")[1].split(",")

    ans = set()
    for w in words:
        pos = text.find(w)
        while pos != -1:
            for i in range(len(w)):
                ans.add(pos + i)
            pos = text.find(w, pos + 1)

        w = w[::-1]
        pos = text.find(w)
        while pos != -1:
            for i in range(len(w)):
                ans.add(pos + i)
            pos = text.find(w, pos + 1)

    print(len(ans))
