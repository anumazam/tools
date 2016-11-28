#!/usr/bin/python

# this is a tool for randomly assigning wells for samples on a 96 well plate.

# create vectors for rows and columns
columns = []
for n in range(1, 13, 1):
    columns.append(n)

rowIDs = [ 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H' ]
A = ['1', '2', '3', '1', '2', '3', '1', '2', '3', '1', '2', '3', ]
B = []
C = []
D = []
E = []
F = []
G = []
H = []

# create table for plate
print "\n"
from tabulate import tabulate
print tabulate ([ A, B, C, D, E, F, G, H ], headers = columns, showindex = rowIDs, numalign = "center")
print "\n"

numstrains = input("How many strains will you distribute on this plate? ")
numsamples = 96/numstrains
print "There will be " + str(numsamples) + " samples per strain."

strainsvector=[]
for n in range(1,numstrains+1,1):
    strainsvector.append(n)

print strainsvector

