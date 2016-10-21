# imports the aargument variable option
from sys import argv

# specifies the argv
script, filename = argv

# saves filename file as txt variable
txt = open(filename)

print "Here's your file %r:" % filename
# uses a function that reads out and prints the file saved in the txt variable
print txt.read()

print "Type the filename again:"
# speciefies the txt file name with a raw input
file_again = raw_input("> ")

# open the same file as before, but with a different method
txt_again = open(file_again)

# use a file function to read and afterwards print the contents of filename
print txt_again.read()

txt.close()
txt_again.close()
