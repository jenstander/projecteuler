import math

sums = 0
sumofsquares = 0

for i in range(1,101):
  sumofsquares += math.pow(i,2)
  sums += i

squareofsums = math.pow(sums,2)

diffence =  squareofsums - sumofsquares
print "square"
print squareofsums
print "sum"
print sumofsquares 
print "difference"
print diffence

