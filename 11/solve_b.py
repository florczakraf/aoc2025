#!/usr/bin/env pypy3
import sys

lines = sys.stdin.read().splitlines()
nodes = {}

for l in lines:
    source, dests = l.split(": ")
    nodes[source] = dests.split()

def dfs_counter(s, t, seen):
    if s == t:
        return 1

    if s in seen:
        return seen[s]

    paths = 0
    for next in nodes.get(s, []):
        paths += dfs_counter(next, t, seen)

    seen[s] = paths
    return paths

def dfs_path(s, t, seen):
    if s == t:
        return [[t]]

    if s in seen:
        return seen[s]

    paths = []
    for next in nodes.get(s, []):
        subpaths = dfs_path(next, t, seen)
        for p in subpaths:
            paths.append([s] + p)

    seen[s] = paths
    return paths

print("svr->fft", dfs_counter("svr", "fft", {}))
print("fft->out", dfs_counter("fft", "out", {}))
print()
print("svr->dac", dfs_counter("svr", "dac", {}))
print("dac->out", dfs_counter("dac", "out", {}))
print()
print("dac->fft", dfs_counter("dac", "fft", {}))
print("fft->dac", dfs_counter("fft", "dac", {}))
paths_to_fft = dfs_path("svr", "fft", {})
paths_from_fft_to_dac = dfs_path("fft", "dac", {})
n_paths_from_fft = dfs_counter("fft", "out", {})
total = 0
print(len(paths_to_fft))
for p in paths_to_fft:
    if "dac" in p:
        total += 1
total *= n_paths_from_fft
print(total)
