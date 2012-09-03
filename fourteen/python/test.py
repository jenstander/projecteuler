import math
skip = []
results = [0] * 1000001

def get_totals(n):
	nums = 0
	while n > 1:
		nums += 1
		#skip.append(n)
		if n % 2 == 0:
			n = n/2
		else:
			n = (3*n) + 1
	return nums

for i in range(1000000, 1, -1):
	if i not in skip:
		results[i] = get_totals(i)

hi = max(results)
ind = results.index(hi)
print ind
