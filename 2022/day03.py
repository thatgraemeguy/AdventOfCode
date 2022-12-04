#!/usr/bin/env python3

with open('data/03.txt') as f:
    rucksacks = f.read().splitlines()

def priority(item):
    return ord(item) - 38 if ord(item) < 91 else ord(item) - 96

total_priority = 0
for rucksack in rucksacks:
    first_half = rucksack[:(len(rucksack)//2)]
    second_half = rucksack[(len(rucksack)//2):]
    common = list(set(first_half).intersection(second_half))
    total_priority += priority(common[0])

print(f"Part 1: {total_priority}")

def make_groups(lst, groupsize):
    for i in range(0, len(lst), groupsize):
        yield lst[i:i+groupsize]

total_priority = 0
for group in make_groups(rucksacks, 3):
    group_item = list(set(group[0]).intersection(group[1], group[2]))
    total_priority += priority(group_item[0])

print(f"Part 2: {total_priority}")
