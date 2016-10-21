# import package
from sys import argv

# specify the arguments that will need to be passed into the function
script, filename = argv

# simple printing with one reference
print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you want that, hit RETURN."

# raw input that makes the script to run further once you hit ENTER
# CTRL-C would interrupt the process,therefore not leading to deleting the file
raw_input("?")

# assign file to variable
# the 'w' in the open func stands for "write", default is "read"
print "Opening the file..."
target = open(filename, 'w')

# truncate whole text file
# not necessary, since 'w' in open already trucates automatically
print "Truncating the file. Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."

# assign raw input vaules to variables
line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

# write those variables in the empty file, each in a new row
# target.write(line1)
# target.write("\n")
# target.write(line2)
# target.write("\n")
# target.write(line3)
# target.write("\n")

target.write(line1 + "\n" + line2 + "\n" + line3 + "\n")

print "And finally, we close it."
# close the file
target.close()
