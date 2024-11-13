#!/usr/bin/env python3

def power(creature: str) -> int:
    if creature == "B":
        return 1
    if creature == "C":
        return 3
    if creature == "D":
        return 5
    return 0

if __name__ == "__main__":
    text = input()

    ans = 0
    for i in range(0, len(text), 3):
        ans += power(text[i]) + power(text[i+1]) + power(text[i+2])
        numX = len([c for c in text[i:i+3] if c == "x"])
        ans += max(0, 6 - 4 * numX)

    print(ans)
