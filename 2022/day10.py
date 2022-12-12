#!/usr/bin/env python3

with open('data/10.txt') as f:
    input = f.read().splitlines()


X = 1
cycle = 1
addx = {}
strength = 0
crt=''

while input or addx:
    if cycle == 20 or (cycle % 40) - 20 == 0:
        strength += cycle * X

    crt += "#" if (cycle % 40) - 1 in range(X-1, X+2) else "."

    if cycle in addx.keys():
        X += addx.pop(cycle)
    else:
        instruction = input.pop(0)
        match instruction.split(' '):
            case ['addx', val]:
                addx[cycle+1] = int(val)
            case ['noop']:
                pass
    cycle += 1


print(f"Part1: signal strength = {strength}")

cols = 40
lines = 6
print("Part 2:")
print('\n'.join([crt[a*cols:cols*(a+1)] for a in range(0, lines)]))