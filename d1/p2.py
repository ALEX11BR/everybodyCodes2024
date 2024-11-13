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
    for i in range(0, len(text), 2):
        ans += power(text[i]) + power(text[i+1]) + (0 if "x" in text[i:i+2] else 2)

    print(ans)
