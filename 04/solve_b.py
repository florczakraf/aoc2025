#!/usr/bin/env python3
import sys

total = 0


map = [list(l) for l in sys.stdin.read().splitlines()]

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


try_again = True

while try_again:
    try_again = False
    for y in range(len(map)):
        for x, c in enumerate(map[y]):
            if c == "@":
                remove = is_accessible(y, x)
                if remove:
                    total += 1
                    map[y][x] = "."
                    try_again = True


print(total)
