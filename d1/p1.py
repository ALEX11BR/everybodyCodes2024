#!/usr/bin/env python3

if __name__ == "__main__":
    text = input()

    ans = 0
    for c in text:
        if c == "B":
            ans += 1
        elif c == "C":
            ans += 3

    print(ans)
