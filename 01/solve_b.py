#!/usr/bin/env python3
import sys

zeros = 0
prev = dial = 50

for line in sys.stdin.read().splitlines():
    rot = int(line[1:])
    full, rot = divmod(rot, 100)
    zeros += full
    match line[0]:
        case 'L':
            dial -= rot
        case 'R':
            dial += rot

    if dial < 0 and prev != 0 or dial > 100:  # negative dimod sucks
        zeros += 1

    dial %= 100
    if dial == 0:
        zeros += 1

    prev = dial


print(zeros)
