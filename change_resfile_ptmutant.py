#!/usr/bin/python

# this is a script to generate a point mutation resfile for every residue in a structure.

numres = input("How many residues does your structure have? ")

for i in range(numres):
    x = str(i+1)
    tempfilename = ("res" + x + ".res")

    f = open(tempfilename, "w+")
    f.write("NATAA \nSTART \n* A NATAA \n" + x + " A ALLAA")
    f.close