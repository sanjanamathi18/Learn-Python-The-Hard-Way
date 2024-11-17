from __future__ import annotations

from sys import exit


def gold_room():
    print('This room is full of gold. How much do you take?')

    choice = input('> ')
    if choice.isnumeric():
        how_much = int(choice)
    else:
        dead('Man, learn to type a number.')

    if how_much < 50:
        print("Nice, you're not greedy!")
        exit(0)
    else:
        dead('You greedy bastard!')


def dead(why):
    print(why, 'Good job!')
    exit(0)


gold_room()
