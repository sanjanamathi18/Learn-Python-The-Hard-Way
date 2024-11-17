# this one is like your scrips with argv
from __future__ import annotations


def print_two(*args):  # *args this function allows to pass mutliple arguments
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")

    # print(f"all the arguments{args}")
    # x =" "
    # for a in args:
    # x+=a + ","
    # print(x)


# ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

# this just takes one argument


def print_one(arg1):
    print(f"arg1: {arg1}")

# this one takes no arguments


def print_none():
    print("I got nothin'.")

# tuple_ex = ("vimal","sanjana","hello")
# print_two("Zed","Shaw","sanjana","vimal")


print_two('Zed', 'Shaw')
print_two_again('Zed', 'Shaw')
print_one('First!')
print_none()


# print_one("Hello")
# print(tuple_ex) - "prints with brackets and quotes"
# for x in tuple_ex: - "to print without brackets and quotes"
# print(x,end=",")
