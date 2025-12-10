#!/usr/bin/env python3
import sys
from collections import deque

problems = sys.stdin.read().splitlines()
total = 0

def make_button(bit_indices):
    mask = 0
    for i in bit_indices:
        mask |= (1 << int(i))
    return mask

def bfs(target, buttons):
    q = deque()
    seen = set()
    q.append(([], 0))
    while q:
        steps, v = q.popleft()
        if v == target:
            return len(steps)

        for b in buttons:
            next = v ^ b
            if next in seen:
                continue
            q.append((steps + [b], next))
            seen.add(next)

for p in problems:
    lights, *wirings, _ = p.split()
    target = int(lights[1:-1].replace(".", "0").replace("#", "1")[::-1], 2)
    buttons = [make_button(w[1:-1].split(",")) for w in wirings]

    total += bfs(target, buttons)

print(total)
