#!/usr/bin/env pypy3
import sys

points = [tuple(int(x) for x in l.split(",")) for l in sys.stdin.read().splitlines()]

best = 0
for i, (x, y) in enumerate(points[:-1]):
    for (xx, yy) in points[i + 1:]:
        area = (abs(x - xx) + 1) * (abs(y - yy) + 1)
        if area > best:
            best = area

print(best)
