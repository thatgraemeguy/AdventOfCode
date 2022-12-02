#!/usr/bin/env python3

with open('data/02.txt') as f:
    rounds = f.read().splitlines()


def translate_play(play):
    match play:
        case 'A' | 'X':
            return 'Rock'
        case 'B' | 'Y':
            return 'Paper'
        case 'C' | 'Z':
            return 'Scissors'


def my_score(elf, me):
    match me:
        case 'Rock':
            shape_score = 1
        case 'Paper':
            shape_score = 2
        case 'Scissors':
            shape_score = 3

    match elf, me:
        case ('Rock', 'Scissors') | ('Paper', 'Rock') | ('Scissors', 'Paper'):
            result_score = 0
        case ('Rock', 'Rock') | ('Paper', 'Paper') | ('Scissors', 'Scissors'):
            result_score = 3
        case ('Rock', 'Paper') | ('Paper', 'Scissors') | ('Scissors', 'Rock'):
            result_score = 6

    return shape_score + result_score


total_score = 0

for elf_play, my_play in [x.split() for x in rounds]:
    total_score += my_score(translate_play(elf_play), translate_play(my_play))

print(f"Part 1: my score is {total_score}")


def translate_outcome(outcome):
    match outcome:
        case 'X':
            return 'Loss'
        case 'Y':
            return 'Draw'
        case 'Z':
            return 'Win'


def decide_my_play(elf, outcome):
    match elf, outcome:
        case ('Rock', 'Loss') | ('Paper', 'Win') | ('Scissors', 'Draw'):
            return 'Scissors'
        case ('Rock', 'Win') | ('Paper', 'Draw') | ('Scissors', 'Loss'):
            return 'Paper'
        case ('Rock', 'Draw') | ('Paper', 'Loss') | ('Scissors', 'Win'):
            return 'Rock'


total_score = 0

for elf_play, desired_outcome in [x.split() for x in rounds]:
    total_score += my_score(translate_play(elf_play), decide_my_play(
        translate_play(elf_play), translate_outcome(desired_outcome)))

print(f"Part 2: my score is {total_score}")
