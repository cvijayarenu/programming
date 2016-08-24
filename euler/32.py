digits = [1,3,4,5,6,7,2, 8, 9]
if sorted(digits, key=int) == range(1,10):
    print "has all"
else:
    print "does not have all"