#!/usr/bin/env python3

import sys

if __name__ == "__main__":
    init = input()
    input()
    texts = sys.stdin.read().splitlines()

    words = set(init.split(":")[1].split(","))
    maxLen = len(max(words, key=len))

    ansMat = [[False] * len(texts[0]) for _ in texts]
    ans = 0
    for y0 in range(len(texts)):
        for x0 in range(len(texts[y0])):
            for step in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
                indices = []
                word = ""
                for i in range(maxLen):
                    indices.append(
                        (y0 + i * step[0], (x0 + i * step[1]) % len(texts[y0])))
                    if indices[i][0] >= len(texts) or indices[i][0] < 0:
                        break
                    word += texts[indices[i][0]][indices[i][1]]
                    if word in words:
                        for id in indices:
                            if not ansMat[id[0]][id[1]]:
                                ans += 1
                                ansMat[id[0]][id[1]] = True
    print(ans)
