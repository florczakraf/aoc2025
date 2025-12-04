#!/usr/bin/env python3
import sys

total = 0


map = sys.stdin.read().splitlines()

def neighbors(y, x):
    for dy in (-1, 0, 1):
        for dx in (-1, 0, 1):
            if 0 <= y + dy < len(map) and 0 <= x + dx < len(map[0]):
                yield y + dy, x + dx

def is_accessible(y, x):
    rolls = 0
    for yy, xx in neighbors(y, x):
        if map[yy][xx] == "@":
            rolls += 1

    return rolls <= 4



for y in range(len(map)):
    for x, c in enumerate(map[y]):
        if c == "@":
            total += is_accessible(y, x)


print(total)
