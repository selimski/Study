# imports functions from sys
from sys import argv

# specifies the input values, which are saved as certain variables
script, input_file = argv

# defines a function that prints the file specified in the input
def print_all(f):
    print f.read()

# defines a function that looks for the first line (0)
def rewind(f):
    f.seek(0)

# defines a function that prints the line specified in line_count
# f.readline() autoincrements the line it was reading,
# that is why it always reads the next one
# the comma at the end of print tells readline() that it shouldn't
# insert an additional \n at the end
def print_a_line(line_count, f):
    print line_count, f.readline(),

# specifies the input file from argv as the current_file variable
current_file = open(input_file)

# print some text
print "First let's print the whole file:\n"

# calls function print_all
print_all(current_file)

# print some text
print "Now let's rewind, kind of like a tape."

# calls function rewind
rewind(current_file)

# print some text
print "Let's print three lines:"

# specifies variable current_line and calls function print a line || 1
# current_line becomes line_count, because it is passed as the first argument
current_line = 1
print_a_line(current_line, current_file)

# updates variable current_line and calls function print a line || 2
# statement x += y stands for x = x + y
current_line += 1
print_a_line(current_line, current_file)

# updates variable current_line and calls function print a line || 3
current_line += 1
print_a_line(current_line, current_file)
