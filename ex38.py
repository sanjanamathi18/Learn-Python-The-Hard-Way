# Doing things to lists
from __future__ import annotations

ten_things = "Apples Oranges Crows Telephone Light Sugar"

print("Wait there are not 10 things in that list. Let's fix that.")

stuff = ten_things.split(" ")
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print("Adding: ", next_one)
    stuff.append(next_one)
    print(f"There are {len(stuff)} items now.")

print("There we go: ", stuff)

print("Let's do some things with stuff.")

print("What is in the position 1: ", stuff[1])
# reverse order of the list, starts with -1
print("What is in the last position: ", stuff[-1])
print(stuff.pop())  # removes last items with empty argument
print("The list separated by space: ", " ".join(stuff))
print("#".join(stuff[3:5]))  # 3:5 range from 3 to 4
sorted = stuff.sort()
print(sorted)  # print "none"
print(stuff)
