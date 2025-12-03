#!/usr/bin/env python3
import sys

total = 0

def find_max(batteries):
    best = 0

    for i, x in enumerate(batteries[:-1]):
        for y in batteries[i+1:]:
            if (cur := (x * 10 + y)) > best:
                best = cur
    return best

for l in sys.stdin.read().splitlines():
    batteries = [int(x) for x in l]
    total += find_max(batteries)

print(total)
