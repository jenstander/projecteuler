import math

i = 1 
nex = 0 
while True: 
	print nex
	#get factors, increment and test that the next in line isnt larger than max - change max by deviding by the next num +1
	inc = 1
	factors = []
	test = False
	while True:
		if nex % inc == 0:
			factors.append(inc)
			if inc != nex/inc:
				factors.append(nex/inc)
		
		inc = inc + 1
		#mx = math.ceil(nex / inc)
		
		if math.ceil(nex/inc) < inc:
			print factors
			#test length
			if len(factors) > 500:
				test = True
			factors = False
			factors = []
			break
	nex = i + nex
	i = i + 1
	if test == True:
		break
