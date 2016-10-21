name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
weight = 180 #lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "He's %d pounds heavy." % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (age, height, weight, age + height + weight)

# transformation equations
inch_to_cm = 2.54
lb_to_kg = 0.45

# height and weight in European numbers
height_cm = height * inch_to_cm # in cm
weight_kg = weight * lb_to_kg # in kg

print "%s weighs %d kilograms." % (name, weight_kg)
print "He's %d cm tall." % height_cm

# new character type: %r - print no matter What
print "I have %r family members that are taller than %s" % (5 - 3, name)
