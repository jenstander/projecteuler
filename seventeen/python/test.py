import numpy as np

def rev(s): return s[::-1] 

longhand = np.array([[1,3],[2,3],[3,5],[4,4],[5,4],[6,3],[7,5],[8,5],[9,4],[10,3],[11,6],[12,6],[13,8],[14,8],[15,7],[16,7],[17,9],[18,8],[19,8],[20,6],[30,6],[40,5],[50,5],[60,5],[70,7],[80,6],[90,6],[100,10],[200,10],[300,12],[400,11],[500,11],[600,10],[700,12],[800,12],[900,11],[1000,11]])

#should have just made two lists and had them start out reversed, but oh wells, this will only add on .00000001 second of time, I already typed all that
search_nums = longhand[:,0]
return_nums = longhand[:,1]
search_nums = rev(search_nums.tolist())
return_nums = rev(return_nums.tolist())

#first check to see if there's an exact match and then go from the top and cycle through redundently doing the same thing

total = 0

def add_number_to_total(num):
	global total
	try:
		i = search_nums.index(num)
		total = total + return_nums[i]
		return True
	except ValueError:
		#next do a backwards loop and grab the first number lower than num
		#add that numbers return to the total, subtract that number from num
		#and send num back through this function
		for index,item in enumerate(search_nums):
			if item < num:
				total = total + return_nums[index]
				add_number_to_total(num - item)
				return True

for i in range(1, 1001):
	add_number_to_total(i)

print total
