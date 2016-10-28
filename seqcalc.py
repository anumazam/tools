#!/usr/bin/python

# this is a tool for calculating DNA volumes for sequencing rxns.

sample = ['sample']
numrxns = input("How many sequencing rxns do you have? ")
firstsample = input("What is the first Quintara ID#? ")
sample.append('AAG' + str(firstsample))

finalDNA = ['finalDNA']
finalH2O = ['finalH2O']
concvector = ['miniprep']

for i in range(2,numrxns+2,1):
	sample.append('AAG' + str(firstsample + i - 1))
	print "Rxn #" + str(i-1)
	conc = input("What is the concentration in ng/ul? ")
	concvector.append(conc)

print "\nTo have 80 ng/ul of each plasmid: \n"

totaldna = 0

for j in range(2, numrxns+2,1):

	finalvolDNA = float(800.0/concvector[j-1])
	finalDNA.append(finalvolDNA)
	
	finalvolH2O = 10.0 - finalvolDNA
	finalH2O.append(finalvolH2O)
	
# create sequencing table
# sample ; QID# ; DNA vol ; ddH2O vol ; primer ; correct?
	

from tabulate import tabulate
print tabulate ([ concvector, finalDNA, finalH2O ], headers = sample, floatfmt=".2f")

