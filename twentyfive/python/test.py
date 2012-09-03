current = 0
nex = 1
inc = 0

while True:
	#print current
	placeholder = current
	current = nex
	nex = nex + placeholder
	inc = inc + 1
	if str(current).__len__() >=  1000:
		print "Term: "+str(inc)
		break
