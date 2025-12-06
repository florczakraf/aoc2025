#!/usr/bin/env python3
import operator
from collections import defaultdict
from functools import reduce

import sys

total = 0

problems = defaultdict(list)
lines = sys.stdin.read().splitlines()
ops = lines[-1].split()
lines = lines[:-1]
cols = max(len(l) for l in lines)
problem = 0
for c in range(cols):
    acc = ""
    for l in lines:
        try:
            acc = acc + l[c]
        except IndexError:
            continue

    acc = acc.strip()
    if acc:
        problems[problem].append(int(acc))
    else:
        problem += 1

for i, op in enumerate(ops):
    match op:
        case "+":
            total += sum(problems[i])
        case "*":
            total += reduce(operator.mul, problems[i], 1)

print(total)
