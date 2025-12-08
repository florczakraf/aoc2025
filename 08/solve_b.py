#!/usr/bin/env pypy3
import sys

edges = {}
nodes = sys.stdin.read().splitlines()
for i in range(len(nodes)):
    for j in range(i + 1, len(nodes)):
        x,y,z = (int(n) for n in nodes[i].split(","))
        xx,yy,zz = (int(n) for n in nodes[j].split(","))
        cost = (x - xx)**2 + (y - yy)**2 + (z - zz)**2
        edges[(nodes[i], nodes[j])] = cost

connected = []
unconnected = set(nodes)
sorted_edges = sorted(edges.items(), key=lambda x: x[1])
op = 0
while len(unconnected) > 1:
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

    op += 1
    unconnected.discard(n1)
    unconnected.discard(n2)

last = unconnected.pop()
print(last)
for ns, _ in sorted_edges[op:]:
    if last in ns:
        print(ns)
        print(int(ns[0].split(",")[0]) * int(ns[1].split(",")[0]))
        break
