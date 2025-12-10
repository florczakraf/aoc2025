#!/usr/bin/env python3
import sys
import z3

problems = sys.stdin.read().splitlines()
total = 0

def make_button(bit_indices):
    return [int(x) for x in bit_indices]

def solve(target, buttons):
    solver = z3.Optimize()
    button_vars = []
    joltage_vars = [z3.Int(f"j{i}") for i in range(len(target))]

    for v in joltage_vars:
        solver.add(v == 0)

    for i, button in enumerate(buttons):
        var = z3.Int(f"b{i}")
        button_vars.append(var)

        for counter in button:
            joltage_vars[counter] += var

        solver.add(var >= 0)

    for i, t in enumerate(target):
        solver.add(joltage_vars[i] == t)

    minimized = solver.minimize(sum(button_vars))
    if solver.check() == z3.sat:
        solution = minimized.value().as_long()
        return solution
    else:
        raise RuntimeError

for p in problems:
    _, *wirings, joltages = p.split()
    target = [int(x) for x in joltages[1:-1].split(",")]
    buttons = [make_button(w[1:-1].split(",")) for w in wirings]
    total += solve(target, buttons)

print(total)
