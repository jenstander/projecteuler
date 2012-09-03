import math

def getlargestdev(nummm):
  x = math.ceil(nummm/2)
  while x > 2:
    x = x-1
    if nummm % x == 0:
      getlargestdev(nummm / x)
      return getlargestdev(x)
  print("prime?:"+str(nummm))

#getlargestdev(600851475143)

def largestfactor(numm):
  x = 2
  while x < numm:
    if numm % x == 0: 
      if isprime(numm/x) == True:
        return numm/x
    x = x+1
  return numm
      

def isprime(test):
  y = 2
  while y < test:
    if test % y == 0:
      return False
    y = y + 1
  return True

print largestfactor(600851475143)
