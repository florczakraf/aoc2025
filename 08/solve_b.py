#!/usr/bin/env pypy3
import sys

edges = {}
nodes = [tuple(int(x) for x in l.split(",")) for l in sys.stdin.read().splitlines()]
n_ops = 10 if len(nodes) == 20 else 1000
costs = set()
for i in range(len(nodes)):
    for j in range(i + 1, len(nodes)):
        x,y,z = nodes[i]
        xx,yy,zz = nodes[j]
        cost = (x - xx)**2 + (y - yy)**2 + (z - zz)**2
        edges[cost] = (nodes[i], nodes[j])
        costs.add(cost)

sorted_costs = sorted(costs)
unconnected = set(nodes)
op = 0
while len(unconnected) > 1:
    n1, n2 = edges[sorted_costs[op]]
    op += 1
    unconnected.discard(n1)
    unconnected.discard(n2)

last = unconnected.pop()
for cost in sorted_costs[op:]:
    if last in edges[cost]:
        print(int(edges[cost][0][0]) * int(edges[cost][1][0]))
        break
