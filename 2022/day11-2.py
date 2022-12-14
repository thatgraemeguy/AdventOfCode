#!/usr/bin/env python3

from functools import reduce
from math import lcm

monkeys = {}

with open('data/11.txt') as f:
    while f:
        l = f.readline()
        if l == '':
            break
        match l.strip().split(' '):
            case ['Monkey', n]:
                monkey = int(n.split(":")[0])
                monkeys[monkey] = {}
                monkeys[monkey]['inspections'] = 0
                monkeys[monkey]['results'] = {}
            case ['Starting', 'items:', *i]:
                monkeys[monkey]['items'] = list(map(int, ''.join(i).split(',')))
            case ['Operation:', 'new', '=', 'old', *op]:
                #HACK, how else do you handle '* old'???
                if op == ['*', 'old']:
                    monkeys[monkey]['opstring'] = '**2'
                else:
                    monkeys[monkey]['opstring'] = ''.join(op)
            case ['Test:', 'divisible', 'by', d]:
                monkeys[monkey]['divisor'] = int(d)
            case ['If', b, 'throw', 'to', 'monkey', i]:
                monkeys[monkey]['results'][eval(b.split(":")[0].title())] = int(i)


#Stop the ints getting stupidly big. If any of the ints grows larger than the LCM of all of them,
#reduce the worry value to the modulo of the large number and the LCM, this leaves a small number
#which still divides the same as the large one
worry_ceiling = reduce(lambda a, b: lcm(a, b), [monkey['divisor'] for monkey in monkeys.values()])

def play_round(allmonkeys, thismonkey):
    for item in thismonkey['items']:
        worry = int(eval(str(item)+thismonkey['opstring'])) % worry_ceiling
        target_monkey = thismonkey['results'][worry % thismonkey['divisor'] == 0]
        allmonkeys[target_monkey]['items'].append(worry)
        thismonkey['inspections'] += 1
    thismonkey['items'] = []


for r in range(1,10001):
    for _, m in monkeys.items():
        play_round(monkeys, m)

print("Part 2: ", reduce(lambda a, b: a * b, sorted([monkeys[i]['inspections'] for i in range(len(monkeys))])[-2:]))
