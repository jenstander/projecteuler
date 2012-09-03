import math

numbers = math.factorial(100)

num_string = str(numbers)
int_list = []

for i in num_string:
	int_list.append(int(i))
total = sum(int_list)
print total
