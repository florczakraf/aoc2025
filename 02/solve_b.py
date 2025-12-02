#!/usr/bin/env pypy3

import sys

total = 0

def is_invalid(i):
    s = str(i)

    for j in range(1, len(s) // 2 + 1):
        pattern = s[:j]
        if s == pattern * (len(s) // j):
            return True

    return False


for range_ in sys.stdin.read().strip().split(","):
    a, b = range_.split("-")
    r = range(int(a), int(b) + 1)
    for i in r:
        if is_invalid(i):
            total += i


print(total)
