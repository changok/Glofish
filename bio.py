import sys
#glofish

FILENAME = sys.argv[1]
WIDTH = int(sys.argv[2]) # width(range) of bar(column)
print "GloshFish chart"
print "Read a file : " + FILENAME

f = open(FILENAME, "r")
lines = f.readlines()
MAX_CHRPOS = 0	# maximum number of rChrPos : generate reasonable number of bars(columns) of chart
NUM_MUTANT = 0	# the number of Mutants
THRESHOLD = 300	# threshold for pretty chart printer
ROMANS = ["I", "II", "III", "IV", "V", "X"]

# first pass: pick up the number of mutant in the input data and the max of rChrPos
for i in lines:
	NUM_MUTANT = max(int(i.split(" ")[0]), NUM_MUTANT)
	MAX_CHRPOS = max(int(i.split(" ")[2]), MAX_CHRPOS)

print "Maximum rChrPos : " + str(MAX_CHRPOS)

NUM_BARS = MAX_CHRPOS / WIDTH	# the number of bars(column) in chart


# initialzing table part
mutants = []
Chrs = []
totals = []	# totals of chr for calculating portion of each bar


# check if there are all Chr exist in each mutant_id
for i in range(NUM_MUTANT):
	mutants.append([])	# appending each Chr array to each mutant
	totals.append([])
	for j in range(6):
		mutants[i].append([])	# appending each rChr array to each Chr
		totals[i].append(0)
		for k in range(NUM_BARS+1):
			mutants[i][j].append(0)

# second pass : increase the count of each ChrPos of each Mutant
for i in lines:
	row = i.split(" ")
	mutant = int(row[0])-1
	index = int(row[2])/WIDTH
	chrnum = -1
	if row[1] == "I": chrnum = 0
	elif row[1] == "II": chrnum = 1
	elif row[1] == "III": chrnum = 2
	elif row[1] == "IV": chrnum = 3
	elif row[1] == "V": chrnum = 4
	elif row[1] == "X": chrnum = 5
	
	if chrnum == -1:
		print "unexpected Chr error"
		sys.exit(0)
	#mutants[mutant number][roman numeral][chrpos]
	mutants[mutant][chrnum][index] += 1
	totals[mutant][chrnum] += 1

# pretty printout part
for i in range(NUM_MUTANT):
	print "\nMUTANT TABLE : mutant_%s" % (i+1)
	for j in range(6):
		compress = totals[i][j]/THRESHOLD +1	# for pretty "bar" printout
		print "Section : %s (Chr)" % ROMANS[j],
		print "	/ total : " + str(totals[i][j])
		if compress > 1:
			print "The length(height) of each bar is compressed(divided) by " + str(compress) + "."
		print "The range of ChrPos on each bar is " + str(WIDTH) + "(base)."
		#print mutants[i][j]
		for k in range(NUM_BARS+1):
			portion = (float(mutants[i][j][k])/float(totals[i][j]))*100.0
			portion = round( portion, 2)
			print str(k+1) + ": " + str(mutants[i][j][k]) + "(" + str(portion) + "%):\t",
			for h in range(mutants[i][j][k]/compress):
				print "|",
			print ""
		print ""
