#!/usr/bin/env python3

if __name__ == "__main__":
    init = input()
    input()
    text = input()

    words = init.split(":")[1].split(",")

    ans = 0
    for w in words:
        pos = text.find(w)
        while pos != -1:
            ans += 1
            pos = text.find(w, pos + 1)

    print(ans)
