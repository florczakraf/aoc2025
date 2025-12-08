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
connected = []
for op in range(n_ops):
    n1, n2 = edges[sorted_costs[op]]
    previously_updated = None
    for i, g in enumerate(connected):
        if n1 in g or n2 in g:
            if not previously_updated:
                g.add(n1)
                g.add(n2)
                previously_updated = i
            else:
                g.update(connected[previously_updated])
                connected.pop(previously_updated)
                break
    else:
        if not previously_updated:
            connected.append({n1, n2})

sc = sorted(connected, key=lambda x: len(x), reverse=True)
print(len(sc[0]) * len(sc[1]) * len(sc[2]))
