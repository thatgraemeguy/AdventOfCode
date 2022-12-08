#!/usr/bin/env python3

from functools import reduce

with open('data/08.txt') as f:
    data = f.read().splitlines()

#data = """
#30373
#25512
#65332
#33549
#35390""".strip().split('\n')

grid = list(map(list, data))

visible = set()
scenic = {}

for r, row in enumerate(grid):
    for c, col in enumerate(row):

        #Trees on the outer edges are always visible
        if r > 0 and r < len(grid)-1 and c > 0 and c < len(row)-1:
            west = [t for t in grid[r][0:c] if t >= grid[r][c]]
            if not west:
                visible.add((r, c))
                #print(f"{r, c} visible from west")

            east = [t for t in grid[r][c+1:] if t >= grid[r][c]]
            if not east:
                visible.add((r, c))
                #print(f"{r, c} visible from east")

            north = [grid[x][c] for x in range(r) if grid[x][c] >= grid[r][c]]
            if not north:
                visible.add((r, c))
                #print(f"{r,c} visible from north")

            south = [grid[x][c] for x in range(r+1, len(grid)) if grid[x][c] >= grid[r][c]]
            if not south:
                visible.add((r, c))
                #print(f"{r,c} visible from south")

        #Scenic score - number of trees of same or lower height in each direction, multipled together
        scenic[(r,c)] = {}
        #west
        if c > 0:
            scenic[(r,c)]['w'] = 0
            for x in range(c-1, -1, -1):
                if grid[r][x] <= grid[r][c]:
                    scenic[(r,c)]['w'] += 1
                if grid[r][x] >= grid[r][c]:
                    break
        
        #east
        if c < len(grid)-1:
            scenic[(r,c)]['e'] = 0
            for x in range(c+1, len(grid)):
                if grid[r][x] <= grid[r][c]:
                    scenic[(r,c)]['e'] += 1
                if grid[r][x] >= grid[r][c]:
                    break

        #north
        if r > 0:
            scenic[(r,c)]['n'] = 0
            for x in range(r-1, -1, -1):
                if grid[x][c] <= grid[r][c]:
                    scenic[(r,c)]['n'] += 1
                if grid[x][c] >= grid[r][c]:
                    break
                
        #south
        if r < len(grid)-1:
            scenic[(r,c)]['s'] = 0
            for x in range(r+1, len(grid)):
                if grid[x][c] <= grid[r][c]:
                    scenic[(r,c)]['s'] += 1
                if grid[x][c] >= grid[r][c]:
                    break


#Part 1: the outer edges are always visible
outer = (2 * len(grid)) + (2 * (len(grid) - 2))

#Part 2:
most_scenic = 0
for tree in scenic:
    most_scenic = max(most_scenic, reduce(lambda a,b: a*b, scenic[tree].values()))

print(f"Part 1: {outer+len(visible)} trees visible")
print(f"Part 2: Highest scenic score: {most_scenic}")