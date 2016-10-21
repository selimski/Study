print "What is your name?",
name = raw_input()
print "How old are you in cm?",
height = int(raw_input())
print "What is your hobby?",
hobby = raw_input()

height_m = height / 100.0

print """
Hi %r %r!
You are really tall!
%r is a lot for a gnome...
""" % (hobby, name, height_m)
