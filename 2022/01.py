#!/usr/bin/env python3

with open('data/01.txt') as f:
    lines = f.read().splitlines()

#lines is a list like ['1000', 3000', '', '5000', ''] for 2 elves

#figure out which indices in the list contain ''
idxs = [idx for idx, val in enumerate(lines, start=1) if val == '']

#slice the list into individual elves using the indices from before
elves = [lines[begin:end-1] for begin, end in zip([0]+idxs, idxs)]

#sum the calories each elf carries, and sort the resulting list in desc order
calcounts = sorted([sum(map(int, elf)) for elf in elves], reverse=True)

print(f"Part 1: {calcounts[0]} calories.")
print(f"Part 2: {sum(calcounts[0:3])} calories.")
