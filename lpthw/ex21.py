def add(a, b):
    print "ADDING %d + %d" % (a, b)
    return a + b

def substract(a, b):
    print "SUBSTRACTING %d - %d" % (a, b)
    return a - b

def multiply(a, b):
     print "MULTIPLYING %d * %d" % (a, b)
     return a * b

def divide(a, b):
    print "DIVIDING %d / %d" % (a, b)
    return a / b


print  "Let's do some math with just functions!"

'''
age = add(30 ,5)
height = substract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)
'''

age = add(1, 98)
height = substract(718.21, 41)
weight = multiply(90324.11, 2325.44)
iq = divide(1000.0, 23332)


print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)


# A puzzle for the extra credit, type it anyway.
print "Here is a puzzle."

what = add(age, substract(height, multiply(weight, divide(iq, 2))))

print "That becomes: ", what, "Can you do it by hand?"

# (30+5)+((78-4)-(((100/2)/2)*(90*2))) = ???
