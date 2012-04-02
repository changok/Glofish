import sys
#glofish

filename = sys.argv[1]
print "GloshFish chart"
print "Read a file : " + filename

f = open(filename, "r")
lines = f.readlines()
WIDTH = 1000000 # width(range) of bar(column)
MAX_CHRPOS = 0	# maximum number of ChrPos : generate reasonable number of bars(columns) of chart
NUM_MUTANT = 0	# the number of Mutants
THRESHOLD = 300	# threshold for pretty chart printer

# first pass: pick up the number of mutant in the input data and the max of ChrPos
for i in lines:
	NUM_MUTANT = max(int(i.split(" ")[0]), NUM_MUTANT)
	MAX_CHRPOS = max(int(i.split(" ")[1]), MAX_CHRPOS)

print "Maximum ChrPos : " + str(MAX_CHRPOS)

NUM_BARS = MAX_CHRPOS / WIDTH	# the number of bars(column) in chart

# initialzing table part
mtable = []
totals = []	# totals of chr for calculating portion of each bar

for i in range(NUM_MUTANT):
	mtable.append([])
	totals.append(0)
	for j in range(NUM_BARS+1):
		mtable[i].append(0)

# second pass: increase the count of each ChrPos of each Mutant
for i in lines:
	row = i.split(" ")
	Chr = int(row[0])-1
	index = int(row[1])/WIDTH
	mtable[Chr][index] += 1
	totals[Chr] += 1

# pretty printout part
for i in range(NUM_MUTANT):
	compress = totals[i]/THRESHOLD +1	# for pretty "bar" printout
	print "MUTANT TABLE : mutant_%s" % (i+1),
	print " / total: " + str(totals[i])
	if compress > 1:
		print "The length of each bar is compressed(divided) by " + str(compress)
	print mtable[i]
	for j in range(NUM_BARS+1):
		portion = (float(mtable[i][j])/float(totals[i]))*100.0
		portion = round( portion, 2)
		print str(mtable[i][j]) + "(" + str(portion) + "%):\t",
		for h in range(mtable[i][j]/compress):
			print "|",
		print ""
