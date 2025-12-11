#!/usr/bin/env pypy3
import sys

lines = sys.stdin.read().splitlines()
nodes = {}

for l in lines:
    source, dests = l.split(": ")
    nodes[source] = dests.split()

seen = {}

def dfs(s):
    if s == "out":
        return 1

    if s in seen:
        return seen[s]

    paths = 0
    for next in nodes[s]:
        paths += dfs(next)

    seen[s] = paths
    return paths

print(dfs("you"))
