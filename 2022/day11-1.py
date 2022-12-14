#!/usr/bin/env python3

from functools import reduce

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


def play_round(allmonkeys, thismonkey):
    for item in thismonkey['items']:
        worry = int(eval(str(item)+thismonkey['opstring'])) // 3
        target_monkey = thismonkey['results'][worry % thismonkey['divisor'] == 0]
        allmonkeys[target_monkey]['items'].append(worry)
        thismonkey['inspections'] += 1
    thismonkey['items'] = []


for r in range(1,21):
    for _, m in monkeys.items():
        play_round(monkeys, m)

print("Part 1: ", reduce(lambda a, b: a * b, sorted([monkeys[i]['inspections'] for i in range(len(monkeys))])[-2:]))
