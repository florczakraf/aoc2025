#!/usr/bin/env python3
import sys

zeros = 0
dial = 50

for line in sys.stdin.read().splitlines():
    rot = int(line[1:])
    match line[0]:
        case 'L':
            dial -= rot
        case 'R':
            dial += rot

    dial %= 100
    if dial == 0:
        zeros += 1

print(zeros)
