import math

# Below is for the actual question, where it's always a cube
def getit(a):
    test = math.factorial(a*2)/math.factorial(a)**2
    print test

getit(20)

# testing non-cube (different number rows than columns
def getittwo(a,b):
    test = math.factorial(a+b)/(math.factorial(a)*math.factorial(b))    
    print test

getittwo(2,4)

# I got help by first figureing out 2 and 3 and then trying to find a good formula :)
# Catching back up on combinations helped, especially the explanation of pascal's triangle
