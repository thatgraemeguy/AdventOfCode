#!/usr/bin/env python3

with open('data/04.txt') as f:
    assignments = f.read().splitlines()

part1 = 0
part2 = 0
for pair in assignments:
    e1, e2 = pair.split(',')
    s1begin, s1end = map(int, e1.split('-'))
    s2begin, s2end = map(int, e2.split('-'))
    s1 = set(range(s1begin, s1end+1))
    s2 = set(range(s2begin, s2end+1))
    if s1.issubset(s2) or s2.issubset(s1):
        part1 += 1
    if not s1.isdisjoint(s2):
        part2 += 1

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")