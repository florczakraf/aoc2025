#!/usr/bin/env pypy3
import sys

lines = sys.stdin.read().splitlines()
nodes = {}

for l in lines:
    source, dests = l.split(": ")
    nodes[source] = dests.split()

def dfs(s, t, seen):
    if s == t:
        return 1

    if s in seen:
        return seen[s]

    paths = 0
    for next in nodes.get(s, []):
        paths += dfs(next, t, seen)

    seen[s] = paths
    return paths

fft_to_dac = dfs("fft", "dac", {})

if fft_to_dac:
    print(dfs("svr", "fft", {}) * fft_to_dac * dfs("dac", "out", {}))
else:
    print(dfs("svr", "dac", {}) * dfs("dac", "fft", {}) * dfs("fft", "out", {}))
