from sys import argv

my_script, item1, item2, item3 = argv

print "Version:", my_script
print "My shopping list: \n*", item1,
item1q = int(raw_input("quantity:"))
print "*", item2,
item2q = int(raw_input("quantity:"))
print "*", item3,
item3q = int(raw_input("quantity:"))

print "All in all there are %s %s, %s %s and %s %s on the list." % (item1, item1q, item2, item2q, item3, item3q)
print "Total of %s products to buy" % (item1q + item2q + item3q)
