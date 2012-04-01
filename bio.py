import commands
import sys

#for i in sys.argv:
#	print str(i)

#commands.getoutput("cat rank.txt | sed 's/\("[0-9]*"\) \("mutant_[1-8]"\) .* \([0-9]*\) ".*" .*/\1 \2 \3/'")

#blah = """cat %s | sed 's/\("[0-9]*"\) \("mutant_[1-8]"\) .* \([0-9]*\) ".*" .*/\1 \2 \3/'""" % sys.argv[1]
#result = commands.getoutput(blah)

f = open("parsedRank.txt", "r")
lines = f.readlines()
WIDTH = 1000000
MAX_CHRPOS = 0 
num_mutant = 8

for i in lines:
	MAX_CHRPOS = max(int(i.split(" ")[1]), MAX_CHRPOS)

print MAX_CHRPOS

num_bar = MAX_CHRPOS / WIDTH

# initialzing part
mtable = []
totals = []
#bars = []
#for i in range(num_bar+1):
	#bars.append(0)

for i in range(num_mutant):
	mtable.append([])
	totals.append(0)
	for j in range(num_bar+1):
		mtable[i].append(0)

for i in lines:
	row = i.split(" ")
	Chr = int(row[0])-1
	index = int(row[1])/WIDTH
	mtable[Chr][index] += 1
	totals[Chr] += 1

for i in range(num_mutant):
	print "MUTANT TABLE : mutant_%s" % (i+1),
	print " / total: " + str(totals[i])
	print mtable[i]
	for j in range(num_bar+1):
		portion = (float(mtable[i][j])/float(totals[i]))*100.0
		portion = round( portion, 2)
		print str(mtable[i][j]) + "(" + str(portion) + "%):\t",
		for h in range(mtable[i][j]):
			print "|",
		print ""
