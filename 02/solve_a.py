#!/usr/bin/env pypy3
import sys

total = 0

def is_invalid(i):
    s = str(i)
    half = len(s)//2
    return s[:half] == s[half:]

for range_ in sys.stdin.read().strip().split(","):
    a, b = range_.split("-")
    r = range(int(a), int(b) + 1)
    for i in r:
        if is_invalid(i):
            total += i

print(total)
