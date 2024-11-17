from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}")

# we could do these two on one line, how?

#in_file = open(from_file)
#indata = in_file.read()
indata = open(from_file).read()
#print(type(indata))
#print(indata)

print(f"The input file is {len(indata)} bytes long")

print(f"Does the output file exist? {exists(to_file)}")
print("Ready, hit RETURN to continue, CTRL-C to abort.")
input() #to get next input from user

#out_file = open(to_file, 'w')
#out_file.write(indata)
out_file = open(to_file).write(indata)

#out_file = open(to_file, 'a')
#out_file.write(f"\n{indata}")
#out_file.write("\n" + indata)


print("Alright, all done.")

#out_file.close()
#in_file.close()