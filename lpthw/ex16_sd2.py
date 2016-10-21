from sys import argv

script, text_file = argv

print "open %r" % text_file
note = open(text_file)

print "read %r" % text_file
print "this is the content of the file:"
content = note.read()
print content

print "that was enough for today"

note.close()
print "file closed, good-bye"
