#!/usr/bin/env python3
import sys

total = 0

def find_max(batteries, n):
    to_remove = len(batteries) - n
    while to_remove:
        for i in range(len(batteries) - 1):
            if batteries[i] < batteries[i+1]:
                batteries = batteries[:i] + batteries[i+1:]
                break
        to_remove -= 1

    return int(batteries[:n])

for l in sys.stdin.read().splitlines():
    m = find_max(l, 12)
    total += m

print(total)
