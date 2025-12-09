#!/usr/bin/env pypy3
import sys
from itertools import pairwise

points = [tuple(int(x) for x in l.split(",")) for l in sys.stdin.read().splitlines()]
edges = [((min(a, c), min(b, d)), (max(a, c), max(b, d))) for (a, b), (c, d) in pairwise(points + [points[0]])]
def intersects():
    x0, x1 = min(x, xx), max(x, xx)
    y0, y1 = min(y, yy), max(y, yy)
    for (xx0, yy0), (xx1, yy1) in edges:
        if x0 < xx1 and y0 < yy1 and x1 > xx0 and y1 > yy0:
            return True

    return False

best = 0
for i, (x, y) in enumerate(points[:-1]):
    for (xx, yy) in points[i + 1:]:
        area = (abs(x - xx) + 1) * (abs(y - yy) + 1)
        if area > best and not intersects():
            best = area

print(best)
