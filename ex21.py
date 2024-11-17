def add(a, b):
    print(f"ADDING {a} + {b}")
    return a + b

def sub(a, b):
    print(f"SUBRACTING {a} - {b}")
    return a - b

def mul(a, b):
    print(f"MULTIPLY {a} * {b}")
    return a * b

def div(a, b):
    print(f"DIVIDE {a} / {b}")
    return a / b


print("Let's do some math with just functions!")

age = add(30, 5)
#age = print(add(5,2))
height = sub(78, 4)
weight = mul(90, 2)
iq = div(100, 2)

print(f" Age: {age}\n Height: {height}\n Weight: {weight}\n IQ: {iq}\n ")


# A puzzle for the extra credit, type it anyway.

print("Here is a puzzle.")

what = add(age, sub(height, mul(weight, div(iq,2))))

print("That becomes: ", what, " CAn you do it by hand?")


