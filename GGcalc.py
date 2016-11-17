#!/usr/bin/python

# this is a tool for setting up equimolar golden gate assembly rxns.

numparts = input("How many part plasmids will you put in your GG rxn? ")
DNAconc = input("How much DNA in ng would you like in your rxn for each part? ")

concvector = []

for i in range(1,numparts+1,1):
	print "Part #" + str(i)
	conc = input("What is the concentration in ng/ul? ")
	concvector.append(conc)
	
print "The concentrations of your parts are " + str(concvector) + "."

print "To have " + str(DNAconc) + " ng of each part plasmid in your GG reaction, add: "

totaldna = 0
for j in range(1, numparts+1,1):
	print "Part #" + str(j)
	finalvol = float(float(DNAconc)/concvector[j-1])
	print finalvol
	totaldna = totaldna + finalvol
	
totalwater = 8 - totaldna
print "Also add .5 ul ligase, .5 ul GG enzyme, 1 ul T4 buffer, and " + str(totalwater) + " ul water."