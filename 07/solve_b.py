#!/usr/bin/env python3
from collections import defaultdict

import sys

beams = {}
lines = sys.stdin.read().splitlines()
beams[(0, lines[0].index("S"))] = 1
for _ in range(len(lines) - 1):
    next_beams = defaultdict(int)
    for (y, x), n in beams.items():
        if lines[y + 1][x] == "^":
            for candidate in ((y + 1, x - 1), (y + 1, x + 1)):
                next_beams[candidate] += n
        else:
            next_beams[(y + 1, x)] += n

    beams = next_beams

print(sum(beams.values()))
