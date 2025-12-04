#!/usr/bin/env pypy3
import sys
#from functools import cache

total = 0


map = [list(l) for l in sys.stdin.read().splitlines()]

#@cache
def neighbors(y, x):
    ns = []
    for dy in (-1, 0, 1):
        for dx in (-1, 0, 1):
            if 0 <= y + dy < len(map) and 0 <= x + dx < len(map[0]):
                ns.append((y + dy, x + dx))
    return ns

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
