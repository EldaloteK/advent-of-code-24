#!/usr/bin/env python3

with open("../input/2ab.txt", "r") as lines:
    lines = [r.strip().split() for r in lines.readlines()]

    part_a_total = 0

    for line in lines:
        # decreasing
        if all(0 < int(line[item]) - int(line[item + 1]) <= 3  for item in range(len(line) - 1)):
            part_a_total += 1
        # incrasing
        if all(0 < int(line[item + 1]) - int(line[item]) <= 3  for item in range(len(line) - 1)):
            part_a_total += 1

    print(part_a_total)

