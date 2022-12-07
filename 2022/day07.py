#!/usr/bin/env python3

with open('data/07.txt') as f:
    cmds = f.read().splitlines()

def dirname(dirs):
    return '/' + '/'.join(list(dirs[1:]))


cd = []
sizes={}
for cmd in cmds:
    match cmd.split():
        case ['$','cd', dir]:
            if dir == '..':
                cd.pop()
            else:
                cd.append(dir)
            if dirname(cd) not in sizes.keys():
                sizes[dirname(cd)] = 0
        case ['$', 'ls']:
            pass
        case ['dir', dir]:
            pass
        case [sz, fn]:
            dpath = dirname(cd).split('/') if len(cd) > 1 else ['/']
            for i in range(1, len(dpath)+1):
                d = dirname(dpath[0:i])
                sizes[d] += int(sz)
                #print(f"{i} {sz} {fn} {cd} {dirname(cd)} {dpath} add {sz} to {d}")
        case _:
            print(f"Unknown: {cmd}")

print(f"Part 1: {sum([x for x in sizes.values() if x < 100000])}")

total_space = 70000000
reqd_space = 30000000
unused_space = total_space - sizes['/']
smallest_dir = reqd_space - unused_space

print(f"Part 2: {min([x for x in sizes.values() if x > smallest_dir])}")