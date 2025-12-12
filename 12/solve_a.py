#!/usr/bin/env python3
import sys

total = 0
lines = sys.stdin.read().splitlines()
boxes = [''.join(lines[i * 5 + 1 : i * 5 + 4]).count("#") for i in range(6)]

for l in lines[30:]:
    dimensions, nums = l.split(": ")
    x, y = dimensions.split("x")
    area = int(x) * int(y)
    nums = [int(n) for n in nums.split()]
    needed = sum(a * b for a, b in zip(nums, boxes))
    total += area >= needed

print(total)
