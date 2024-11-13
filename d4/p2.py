#!/usr/bin/env python3

if __name__ == "__main__":
    nails = []
    try:
        while True:
            nails.append(int(input()))
    except EOFError:
        pass

    minNail = min(nails)
    ans = 0
    for nail in nails:
        ans += nail - minNail

    print(ans)
