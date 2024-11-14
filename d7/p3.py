#!/usr/bin/env python3

from concurrent.futures import ProcessPoolExecutor
from itertools import combinations

RACE = """\
S+= +=-== +=++=     =+=+=--=    =-= ++=     +=-  =+=++=-+==+ =++=-=-=--
- + +   + =   =     =      =   == = - -     - =  =         =-=        -
= + + +-- =-= ==-==-= --++ +  == == = +     - =  =    ==++=    =++=-=++
+ + + =     +         =  + + == == ++ =     = =  ==   =   = =++=
= = + + +== +==     =++ == =+=  =  +  +==-=++ =   =++ --= + =
+ ==- = + =   = =+= =   =       ++--          +     =   = = =--= ==++==
=     ==- ==+-- = = = ++= +=--      ==+ ==--= +--+=-= ==- ==   =+=    =
-               = = = =   +  +  ==+ = = +   =        ++    =          -
-               = + + =   +  -  = + = = +   =        +     =          -
--==++++==+=+++-= =-= =-+-=  =+-= =-= =--   +=++=+++==     -=+=++==+++-\
""".splitlines()


def getFromRace(line: int, column: int) -> str:
    if line < 0 or column < 0 or line >= len(RACE) or column >= len(RACE[line]):
        return " "
    return RACE[line][column]


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


def getScore(race: str, ops: str | list[str]) -> str:
    i = 0
    laps = 0
    powers = []
    while True:
        if i == 0:
            prevPow = 10
        else:
            prevPow = powers[-1]
        powers.append(applyPower(
            prevPow, getPowerOp(ops[i % len(ops)], race[i % len(race)])))
        i += 1
        if i % len(race) == 0:
            laps += 1
        if laps >= 11:
            break
    return sum(powers)


if __name__ == "__main__":
    enemy = input().split(":")[1].split(",")

    race = [RACE[0][1], RACE[0][2]]
    racePoints = set([(0, 1), (0, 2)])
    currentPoint = (0, 2)
    while True:
        for diff in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            newPoint = (currentPoint[0] + diff[0], currentPoint[1] + diff[1])
            if newPoint in racePoints:
                continue
            newElem = getFromRace(newPoint[0], newPoint[1])
            if newElem == " ":
                continue
            race.append(newElem)
            racePoints.add(newPoint)
            currentPoint = newPoint
            break
        if newElem == "S":
            break

    enemyPts = getScore(race, enemy)

    ans = 0
    with ProcessPoolExecutor() as executor:
        futures = []
        for comb in combinations(range(11), 6):
            for minuses in combinations(comb, 3):
                plan = ["+"] * 11
                for i in comb:
                    if i in minuses:
                        plan[i] = "-"
                    else:
                        plan[i] = "="
                futures.append(executor.submit(getScore, race, plan))
        for f in futures:
            if enemyPts < f.result():
                ans += 1

    print(ans)
