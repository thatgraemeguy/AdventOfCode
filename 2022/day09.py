#!/usr/bin/env python3

from util.timing import timeit

class Knot:
    def __init__(self):
        self.row = 1
        self.col = 1
        self.visited_positions = set({(self.row, self.col)})

    def __get_position(self):
        return (self.row, self.col)

    position = property(__get_position)

    def __move_up(self):
        self.row += 1

    def __move_down(self):
        self.row -= 1

    def __move_right(self):
        self.col += 1

    def __move_left(self):
        self.col -= 1

    def move(self, directions: list):
        for direction in directions:
            match direction:
                case 'U':
                    self.__move_up()
                case 'D':
                    self.__move_down()
                case 'R':
                    self.__move_right()
                case 'L':
                    self.__move_left()
                case other:
                    raise ValueError("direction must be 'U', 'D', 'L' or 'R'")
        self.visited_positions.add(self.position)


@timeit
def process_moves(moves, knots):
    for move in moves:
        direction, count = move.split()
        for i in range(int(count)):
            for k in knots.keys():
                if k == 0:
                    #0 = head
                    knots[k].move(direction)
                else:
                    #>0 = tail/s
                    tail = knots[k]
                    head = knots[k-1]
                    #Check where tail is relative to head and move if needed
                    match (tail.row - head.row, tail.col - head.col):
                        #If the head is ever two steps directly up, down, left, or right from
                        #the tail, the tail must also move one step in that direction so it
                        #remains close enough:
                        case (-2, 0):
                            tail.move('U')
                        case (2, 0):
                            tail.move('D')
                        case (0, -2):
                            tail.move('R')
                        case (0, 2):
                            tail.move('L')
                        #Otherwise, if the head and tail aren't touching and aren't in the same
                        #row or column, the tail always moves one step diagonally to keep up:
                        case (-2, -1) | (-1, -2) | (-2, -2):
                            tail.move(['U', 'R'])
                        case (-2, 1) | (-1, 2) | (-2, 2):
                            tail.move(['U', 'L'])
                        case (2, -1) | (1, -2) | (2, -2):
                            tail.move(['D', 'R'])
                        case (2, 1) | (1, 2) | (2, 2):
                            tail.move(['D', 'L'])
                        #head and tail are touching
                        case (0,0) | (0,1) | (0,-1) | (1,1) | (1,0) | (1, -1) | (-1, -1) | (-1, 0) | (-1, 1):
                            pass
                        #debugging
                        case other:
                            print(f"Wait... that's impossible! ({other})")
                            breakpoint()


with open('data/09.txt') as f:
    moves = f.read().splitlines()

p1knots = {i: Knot() for i in range(2)}
process_moves(moves, p1knots)
lastknot = p1knots[len(p1knots)-1]
print(f"Part 1: tail visited {len(lastknot.visited_positions)} unique positions.")

p2knots = {i: Knot() for i in range(10)}
process_moves(moves, p2knots)
lastknot = p2knots[len(p2knots)-1]
print(f"Part 2: tail visited {len(lastknot.visited_positions)} unique positions.")
