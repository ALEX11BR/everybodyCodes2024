#!/usr/bin/env python3

from sys import stdin


def applyPower(prevPow: int, op: str) -> int:
    if op == "=":
        return prevPow
    if op == "+":
        return prevPow + 1
    return max(0, prevPow - 1)


if __name__ == "__main__":
    lines = stdin.read().splitlines()
    chariot = {}
    chariotsPows = {}
    for line in lines:
        elems = line.split(":")
        chariot[elems[0]] = elems[1].split(",")
        chariotsPows[elems[0]] = []

    for i in range(10):
        for c in chariot:
            if i == 0:
                prevPow = 10
            else:
                prevPow = chariotsPows[c][-1]
            chariotsPows[c].append(applyPower(
                prevPow, chariot[c][i % len(chariot[c])]))
    chariots = list(chariot.keys())
    chariots.sort(key=lambda c: sum(chariotsPows[c]), reverse=True)

    ans = "".join(chariots)
    print(ans)
