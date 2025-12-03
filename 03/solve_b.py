#!/usr/bin/env python3
from functools import cache

import sys

total = 0

@cache
def find_max(batteries, i):
    if i == 0:
        return 0

    first_value = batteries[0] * 10 ** (i - 1)
    with_first = first_value + find_max(batteries[1:], i-1)
    if len(batteries) > i and i > 0:
        without_first = find_max(batteries[1:], i)
        return max(with_first, without_first)

    return with_first

for l in sys.stdin.read().splitlines():
    batteries = tuple(int(x) for x in l)
    m = find_max(batteries, 12)
    total += m

print(total)
