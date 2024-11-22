#!/usr/bin/env python3

if __name__ == "__main__":
    text = input().split(",")

    ans = 0
    current_height = 0
    for t in text:
        if t[0] == "U":
            current_height += int(t[1:])
        elif t[0] == "D":
            current_height -= int(t[1:])
        ans = max(ans, current_height)

    print(ans)
