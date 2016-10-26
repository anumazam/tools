#!/usr/bin/python

# this is a tool for setting up equimolar golden gate assembly rxns.

numparts = input("How many part plasmids will you put in your GG rxn? ")

concvector = []

for i in range(1,numparts+1,1):
	print "Part #" + str(i)
	conc = input("What is the concentration in ng/ul? ")
	concvector.append(conc)
	
print "The concentrations of your parts are " + str(concvector) + "."

print "To have 75 ug of each part plasmid in your GG reaction, add: "


for j in range(1, numparts+1,1):
	print "Part #" + str(j)
	finalconc = float(75.0/concvector[j-1])
	print finalconc