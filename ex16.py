from __future__ import annotations

from sys import argv

script, filename = argv

print(f"We're going to erase {filename}.")
print('If you don,t want that, hit CTRL-c (^c).')
print('If you do want that, hit RETURN.')

input('?')

print('Opening the file...')

target = open(filename, 'w')
# target = open(filename, 'r')
# target = open(filename, 'a')

print('Truncating the file. Goodbye!')
target.truncate()
# target.truncate(2)

print("Now I'm going to ask you for three lines.")

line1 = input('line 1: ')
line2 = input('line 2: ')
line3 = input('line 3: ')

print('I,m going to write these to file.')

target.write(line1)
target.write('\n')
target.write(line2)
target.write('\n')
target.write(line3)
target.write('\n')

print('And finally, we close it.')
target.close()
