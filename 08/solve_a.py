#!/usr/bin/env pypy3
import sys

edges = {}
nodes = sys.stdin.read().splitlines()
n_ops = 10 if len(nodes) == 20 else 1000
for i in range(len(nodes)):
    for j in range(i + 1, len(nodes)):
        x,y,z = (int(n) for n in nodes[i].split(","))
        xx,yy,zz = (int(n) for n in nodes[j].split(","))
        cost = (x - xx)**2 + (y - yy)**2 + (z - zz)**2
        edges[(nodes[i], nodes[j])] = cost

connected = []
sorted_edges = sorted(edges.items(), key=lambda x: x[1])
for op in range(n_ops):
    (n1, n2), _ = sorted_edges[op]
    to_combine = []
    for i, g in enumerate(connected):
        if n1 in g or n2 in g:
            g.add(n1)
            g.add(n2)
            to_combine.append(i)
    if not to_combine:
        connected.append({n1, n2})

    if len(to_combine) >= 2:
        sorted_to_combine = sorted(to_combine)
        for i in sorted_to_combine[1:]:
            connected[sorted_to_combine[0]].update(connected.pop(i))

sc = sorted(connected, key=lambda x: len(x), reverse=True)
print(len(sc[0]) * len(sc[1]) * len(sc[2]))
