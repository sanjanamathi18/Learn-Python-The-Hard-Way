from sys import argv

script, input_file = argv

#def print_all(file):

def print_all(f):
    print(f.read())

def rewind(f):
    f.seek(0)

def print_a_line(line_count, f):
    print(line_count, f.readline())

current_file = open(input_file)

print("\nFirst let's print the whole file:\n")

print_all(current_file)

print("\nNow let's rewind, kind of a tape.\n")

rewind(current_file)

print("Let's print three lines:\n")

current_line = 1 
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

#for current_line in range(1,4):
    #print_a_line(current_line,current_file)



# rewind(current_file)
# print(current_file.read())
# current_file.seek(100)

# print(current_file.readline())
# print(current_file.readline())
# print(current_file.readline())

# read returns all the lines in the file as a string and moves to the end of file
# readline returns one line in the file as a string and moves to next line
