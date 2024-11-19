#!/usr/bin/env python3

from sys import stdin

if __name__ == "__main__":
    termites = {}
    for line in stdin.read().splitlines():
        l1 = line.split(":")
        termites[l1[0]] = l1[1].split(",")

    ans = 0
    termitesL = ["A"]
    for _ in range(4):
        newTermites = []
        for t in termitesL:
            newTermites += termites[t]
        termitesL = newTermites

    print(len(termitesL))
