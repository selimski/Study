def func1(*args):
    arg1, arg2 = args
    print "Today you choose: %r as your first argument." % arg1
    print "You didn't choose: %r. You did not... \n" % arg2

func1("Yes","Yaaaauzaaaa")

func1(10 + 2, 9 + 4)

a1 = 1000
a2 = 0.1
func1(a1, a2)

func1(a1 + 1, a2 + 12345)

b1 = "hey"
b2 = "bye"
func1(b1 + "bae", b2 + "BIIITCH")

func1(a1 * 100 + a2, a2)

c1 = raw_input("variable1: ")
c2 = raw_input("variable2: ")
func1(c1, c2)
