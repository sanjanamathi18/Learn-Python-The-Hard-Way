
print("Let's practice everything.")
print('You\'d need to know \'bout escapes with \\ that do:')
print('\n newlines and \t tabs.')

#can leave a line in between

poem = """
\tThe lovely world
with logic so firmly planted  
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

print("---------------")
print(poem)
print("---------------")

five = 10 - 2 + 3 - 6
print(f"This should be five: {five}")

# defining a function named "secret_formula" with arg variable "started" 

# inside fun defining variable jelly_beans, jars, crates 

# if you call this function you gets values ov jelly_beans, jars, crates.

def secret_formula(started):
    print("secret_formula function called with value{}".format(started))
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates

# started --> start_point 

start_point = 10000

# calling function "secret_formula" with arg variavle as "start_point" 
# and passing value "10000"
# and storing results in beans, jars, crates 

beans, jars, crates = secret_formula(start_point)

#remember that this is another way to format a string

#print("With a starting point of: {}" .format(start_point))

#print(f"With a starting point of: {start_point}")

# it's just like with an f" " string

print(f"We'd have {beans} beans, {jars} jars, and {crates} crates.")

start_point = start_point / 10

print("We can also do that this way:")

formula = secret_formula(start_point)

#this is an easy to way to apply a list to a format string

print("We'd have {} beans, {} jars, and {} crates.".format(*formula))