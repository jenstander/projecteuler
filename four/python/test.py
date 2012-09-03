def findlargepalendrom():
  x = 999
  pals = []
  while x > 99:
    result = getlargestyforcurrentx(x)
    # add to a list or array or whateve
    if result != 0:
      pals.append(int(result))
    x = x-1
  pals.sort()
  print "The winner is:"
  print pals[-1]

def getlargestyforcurrentx(x):
  y = x 
  while y > 99:
    test = str(y * x)
    #check to see if palendrome
    testreverse = test[::-1]
    if testreverse == test:
      print testreverse
      return testreverse
    y = y-1
  return 0

findlargepalendrom()

