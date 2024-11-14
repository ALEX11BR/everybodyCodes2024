#!/usr/bin/env python3

from sys import stdin

RACE = """\
S-=++=-==++=++=-=+=-=+=+=--=-=++=-==++=-+=-=+=-=+=+=++=-+==++=++=-=-=--
-                                                                     -
=                                                                     =
+                                                                     +
=                                                                     +
+                                                                     =
=                                                                     =
-                                                                     -
--==++++==+=+++-=+=-=+=-+-=+-=+-=+=-=+=--=+++=++=+++==++==--=+=++==+++-\
""".splitlines()


def applyPower(prevPow: int, op: str) -> int:
    if op == "=":
        return prevPow
    if op == "+":
        return prevPow + 1
    return max(0, prevPow - 1)


def getPowerOp(chariotOp: str, globalOp: str) -> str:
    if globalOp == "-":
        return "-"
    if globalOp == "+":
        return "+"
    return chariotOp


if __name__ == "__main__":
    lines = stdin.read().splitlines()
    chariot = {}
    chariotsPows = {}
    for line in lines:
        elems = line.split(":")
        chariot[elems[0]] = elems[1].split(",")
        chariotsPows[elems[0]] = []

    race = []
    for i in range(1, len(RACE[0])):
        race.append(RACE[0][i])
    for i in range(1, len(RACE)):
        race.append(RACE[i][-1])
    for i in range(len(RACE[0]) - 2, 0, -1):
        race.append(RACE[-1][i])
    for i in range(len(RACE) - 1, -1, -1):
        race.append(RACE[i][0])

    i = 0
    laps = 0
    while True:
        for c in chariot:
            if i == 0:
                prevPow = 10
            else:
                prevPow = chariotsPows[c][-1]
            chariotsPows[c].append(applyPower(
                prevPow, getPowerOp(chariot[c][i % len(chariot[c])], race[i % len(race)])))
        i += 1
        if i % len(race) == 0:
            laps += 1
        if laps >= 10:
            break
    chariots = list(chariot.keys())
    chariots.sort(key=lambda c: sum(chariotsPows[c]), reverse=True)

    ans = "".join(chariots)
    print(ans)
