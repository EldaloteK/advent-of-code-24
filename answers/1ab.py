#!/usr/bin/env python3

with open("../input/1ab.txt", "r") as lists:
    lists = [r.strip().split() for r in lists.readlines()]

    first_list = [int(s[0]) for s in lists]
    second_list = [int(s[1]) for s in lists]

    first_list.sort()
    second_list.sort()

    part_a_total = 0
    part_b_total = 0

    for k in range(len(first_list)):
        part_a_total += abs(first_list[k]-second_list[k])
        part_b_total += (first_list[k] * second_list.count(first_list[k]))

    print(part_a_total)
    print(part_b_total)
