# What if
from __future__ import annotations

people = 20
cats = 30
dogs = 15

if people < cats:
    print('Too many cats! The world is doomed!')

if people > cats:
    print('Not too mant cats! The world is saved!')

if people < dogs:
    print('The world is drooled on!')

if people > dogs:
    print('The world is dry!')


dogs += 5

if people >= dogs:
    print('People are greater than or equal to dogs.')

# if people <= dogs or people == cats:
# print(" True ")
# else:
    # print("False")

# print((people <= dogs or people == cats))

if people == dogs:
    print('People are dogs.')
