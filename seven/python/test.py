import math


def isprime(test):
	y = 2
	while y <= math.sqrt(test):
		if test % y == 0:
			return False
		y = y + 1
	return True

def find_squares(maxsize):
	a = []
	x = 2

	while len(a) < maxsize:
		if isprime(x) == True:
			a.append(x)
		x = x + 1
	return a

z = find_squares(10001)

#for item in z:
#	print item

print max(z)

