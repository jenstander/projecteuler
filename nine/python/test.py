# right angle triangle where length of sides == 1000
# brainstorming, rules:
# if a is even, b is odd and other way around
# for this, all are primitave numbers

import math

def get_that_triangle(side_sum):
	a = 1 #side_sum  / 2 #it's certainly not going to be lower than that
	
	while a < side_sum:
		b_range = range(a + 1, side_sum, 2)
		for b in b_range:
			c_square = a**2 + b**2
			print a
			print b
			print math.sqrt(c_square)
			#need to alter below to make sure it has only 0 in decimal, but it works, need to multiply a b and c for number to submit, but really has nothing todo with the functionality
			if a + b + math.sqrt(c_square) == side_sum:
				print a
				print b
				print math.sqrt(c_square)
				return()
		a = a + 1
	
get_that_triangle(1000)
