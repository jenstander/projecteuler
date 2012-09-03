import csv
import string

namereader = csv.reader(open('names.txt','rb'),delimiter=',',quotechar='"')

for names in namereader:
	print len(names)
	names.sort()
	scores = 0
	#scores = []
	inc = 0
	for name in names:
		inc = inc + 1
		points = 0 
		for letter in name:
			i =  string.letters.index(letter) - 25
			points = points + i
		#points = points * inc
		#scores.append(points)
		scores = scores + (points*inc)

#don't need the following
#sortsc = sorted(scores)
#topscore = sortsc.pop()
#ind = scores.index(topscore)
#topname = names[ind]
#print topname
print scores
