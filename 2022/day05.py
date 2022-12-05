#!/usr/bin/env python3

import re

p1stacks = {
    1: list('NCRTMZP'),
    2: list('DNTSBZ'),
    3: list('MHQRFCTG'),
    4: list('GRZ'),
    5: list('ZNRH'),
    6: list('FHSWPZLD'),
    7: list('WDZRCGM'),
    8: list('SJFLHWZQ'),
    9: list('SQPWN'),
}

with open('data/05.txt') as f:
    moves = [list(map(int,re.findall(r"[0-9]+", m))) for m in f.read().splitlines() if bool(re.match(r"^move", m))]

for move in moves:
    times, src, dst = move
    c = 0
    while c < times:
        p1stacks[dst].append(p1stacks[src].pop())
        c += 1

part1 = ''.join([p1stacks[s][-1] for s in p1stacks])

print(part1)

p2stacks = {
    1: list('NCRTMZP'),
    2: list('DNTSBZ'),
    3: list('MHQRFCTG'),
    4: list('GRZ'),
    5: list('ZNRH'),
    6: list('FHSWPZLD'),
    7: list('WDZRCGM'),
    8: list('SJFLHWZQ'),
    9: list('SQPWN'),
}

for move in moves:
    times, src, dst = move
    c = 0
    t = []
    while c < times:
        t.append(p2stacks[src].pop())
        c += 1
    t.reverse()
    p2stacks[dst] += t


part2 = ''.join([p2stacks[s][-1] for s in p2stacks])

print(part2)