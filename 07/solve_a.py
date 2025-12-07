#!/usr/bin/env python3
import sys

splits = 0
beams = set()
lines = sys.stdin.read().splitlines()
beams.add((0, lines[0].index("S")))
for _ in range(len(lines) - 1):
    next_beams = set()
    for y, x in beams:
        if lines[y + 1][x] == "^":
            splits += 1
            next_beams.add((y + 1, x - 1))
            next_beams.add((y + 1, x + 1))
        else:
            next_beams.add((y + 1, x))
    beams = next_beams
print(splits)
