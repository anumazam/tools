#!/usr/bin/python

# this is a tool for calculating DNA volumes for sequencing rxns.

numrxns = input("How many sequencing rxns do you have? ")

concvector = []
for i in range(1,numrxns+1,1):
	print "Rxn #" + str(i)
	conc = input("What is the concentration in ng/ul? ")
	concvector.append(conc)

print "\nTo have 80 ng/ul of each plasmid, add: \n"

totaldna = 0

for j in range(1, numrxns+1,1):
	print "Rxn #" + str(j)
	finalvolDNA = float(800.0/concvector[j-1])
	finalvolH2O = 10.0 - finalvolDNA
	
	format(finalvolDNA, '.2f')
	format(finalvolH2O, '.2f')
	
	print "%.2f" % finalvolDNA + " ul DNA and " + "%.2f" % finalvolH2O + " ul ddH2O. \n"