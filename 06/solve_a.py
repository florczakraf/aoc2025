#!/usr/bin/env python3
import operator
from collections import defaultdict
from functools import reduce

import sys

total = 0

columns = defaultdict(list)
lines = sys.stdin.read().splitlines()
for line in lines:
    items = line.split()
    try:
        for i, item in enumerate(items):
            columns[i].append(int(item))
    except ValueError:
        for i, item in enumerate(items):
            match item:
                case "+":
                    total += sum(columns[i])
                case "*":
                    total += reduce(operator.mul, columns[i], 1)
print(total)
