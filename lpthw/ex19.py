# create a function that takes in 2 arguments and prints out the numbers
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheeses!" % cheese_count
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "Man that's enough for a party!"
    print "Get a blanket.\n"

# in this case the arguments of the function
# are passed directly in a form of numbers
print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)

# variables from the script are passed as the argumetns of the function
print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# a matematical calculation is passed on as the argument
print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)

# the numerical variables are elements of a calaculation, that is the argument
print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
