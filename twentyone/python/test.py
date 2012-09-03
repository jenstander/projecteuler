import math

sums = []
amicable_nums = []
for i in range(1,10000): 
	#print i
	inc = 1
	factors = []
	test = False
	while True:
		if i % inc == 0:
			factors.append(inc)
			if inc != i/inc:
				factors.append(i/inc)
		
		inc = inc + 1
		#mx = math.ceil(nex / inc)
		
		if math.ceil(i/inc) < inc:
			factors.remove(i)
			#print factors
			factor_sums = sum(factors)
			r = -1
			try:
				while 1:
					r = sums.index(i, r+1)
					index = r + 1
					#the current number was a sum of some other numbers devisors
					if factor_sums != i and factor_sums == index:
						amicable_nums.append(index)
						amicable_nums.append(i)
					if i == 2924:
						print i
						print factor_sums
						print index
						print sums.count(i)
			except ValueError:
				pass
			sums.append(factor_sums)

			factors = False
			factors = []
			break
#print sums
print amicable_nums
print sum(amicable_nums)


