#!/usr/bin/env python3
import sys

total = 0

ranges = []
items = []
lines = sys.stdin.read().splitlines()
collecting_ranges = True
for line in lines:
    if not line:
        collecting_ranges = False
        continue

    if collecting_ranges:
        a, b = line.split("-")
        ranges.append(range(int(a), int(b) + 1))
    else:
        item = int(line)
        for r in ranges:
            if item in r:
                total += 1
                break

print(total)
