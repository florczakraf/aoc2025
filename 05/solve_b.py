#!/usr/bin/env python3
import sys

total = 0

points = []
lines = sys.stdin.read().splitlines()
for line in lines:
    if not line:
        break

    a, b = line.split("-")
    points.append((int(a), 1))
    points.append((int(b) + 1, -1))

points.sort()

start = 0
counter = 0
for p, v in points:
    if not counter:
        start = p

    counter += v

    if not counter:
        total += (p - start)

print(total)
