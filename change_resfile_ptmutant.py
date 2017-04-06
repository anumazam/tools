#!/usr/bin/python

# this is a script to generate a point mutation resfile for every residue in a structure.

chainletter_list = ["A", "B", "C", "D", "E"]

numchains = input("How many chains does your structure have? ")
for j in range(numchains):
    
    chainletter = chainletter_list[j]

    numres = input("How many residues does your chain " + chainletter + " have? ")

    for i in range(numres):
        x = str(i+1)
        tempfilename = ("res" + x + ".res")

        f = open(tempfilename, "w+")
        f.write("NATAA \nSTART \n* A NATAA \n" + x + " " + chainletter + " ALLAA")
        
        f.close