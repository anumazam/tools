#!/usr/bin/python

# calculate percent enrichment for each residue for a position in a designed loop

from Bio import SeqIO

nativeseq = raw_input("What is the native sequence? ")
seqfile = raw_input("What is the name of your sequences file? ")
path = raw_input("Where are your files? ~/Dropbox/Research/Structures/transcription_factor/lacI/")
path = "/Users/anumglasgow/Dropbox/Research/Structures/transcription_factor/lacI/" + path + "/" + seqfile

def createResGroup(input_name, input_value):
    input_name = input_value

numres = len(nativeseq)

seqIDs = []
sequences = []

for seq_record in SeqIO.parse(path, "fasta"):
    seqIDs.append(seq_record.id)
    sequences.append(str(seq_record.seq))

all_residues = ["G", "A", "L", "M", "F", "W", "K", "Q", "E", "S", "P", "V", "I", "C", "Y", "H", "R", "N", "D", "T"]
#G = 0
#A = 0
#L = 0
#M = 0
#F = 0
#W = 0
#K = 0
#Q = 0
#E = 0
#S = 0
#P = 0
#V = 0
#I = 0
#C = 0
#Y = 0
#H = 0
#R = 0
#N = 0
#D = 0
#T = 0
#temp = 0

residues = []

for n in range(0, len(sequences)):
    residues.append(sequences[n][0])

for m in range(1, len(all_residues) + 1):
    for n in range(1, len(residues) + 1):
        if all_residues[m - 1] == residues[n - 1]:
            temp += 1
            print "all_residues[m-1] " + all_residues[m - 1]
            print "temp " + str(temp)
    temp = 0

#        createResGroup(str(all_residues[m]), temp)
#        print str(G) + " " + str(S) + " " + str(T)