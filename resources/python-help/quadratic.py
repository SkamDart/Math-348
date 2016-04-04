#!/usr/bin/python

import sys

print 'Number of arguments:', len(sys.argv), 'arguments.'
print 'Argument List:', str(sys.argv)

def quad(a,b,c):
	pos = (-b + math.sqrt(b**2 - 4*a*c)) / (2 * a)
	neg = (-b - math.sqrt(b**2 - 4*a*c)) / (2 * a)

	print "Positive Root of (%d,%d,%d) = " % (a,b,c,pos)
	print "Negative Root of (%d,%d,%d) = " % (a,b,c,neg)
def main(argv):
	a = argv[1]
	b = argv[2]
	c = argv[3]

	quad(a,b,c)

if __name__ == "__main__":
   main(sys.argv[1:])