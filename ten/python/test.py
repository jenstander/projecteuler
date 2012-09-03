import math

def sum_primes(max_number):
	primes = []
	x = 2
	while x < max_number:
		if isprime(x) == True:
			primes.append(x)
		x = x + 1
	return sum(primes)

def isprime(test):
	y = 2
	while y <= math.sqrt(test):
		if test % y == 0:
			return False
		y = y + 1
	return True


print sum_primes(2000000)
