from __future__ import annotations
types_of_people = 10
x = f"There are {types_of_people} types of people."

# x = "there are {} types of people."

binary = 'binary'
do_not = "don't"
y = f'Those who know {binary} and those who {do_not}.'

print(x)

# print(x.format(types_of_people))
# print(x.format(20))

print(y)

print(f"I said: {x}")

# print(f"I said: {x.format()}")

print(f"I also said: '{y}'")

hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"

# joke_evaluation = f"Isn't that joke so funny?! {hilarious}"
# print(joke_evaluation)
# print(joke_evaluation.format(True))

print(joke_evaluation.format(hilarious))

w = 'This is the left side of...'
e = 'a string with a right side.'

print(w + e)
