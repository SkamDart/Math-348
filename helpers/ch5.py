#!/usr/bin/python
from fractions import gcd

def main():
	solution_checker(588,231,63)

def solution_checker(a,b,c):
	
	for i in range(-100,100):
		x = (6 + 11 * i)
		y = (-15 - 28 * i)
		if (a*x) + (b*y) != c:
			print "incorrect solution"
			print "%d + %d != %d" % (x,y,c)
			break
		else:
			print "%d + %d = %d" % (x,y,c)

			gcdResult = gcd(a,b)
			divideResult = c/float(gcdResult)
	print "gcd: %d " % gcdResult
	print "%d/gcd(%d,%d) = %f" % (c,a,b,divideResult)

main()