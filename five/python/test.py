def checkit(number):
  for i in range (2,21):
    testrem = number % i
    if testrem != 0:
      return False
  return True

test = False
number = 40 #probably a much better place to start but whatevs
while test == False:
  number = number + 1
  test = checkit(number)
print number
