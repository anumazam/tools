#!/usr/bin/python

# calculate percent enrichment for each residue for a position in a designed loop

from Bio import SeqIO
import matplotlib.pyplot as plt

nativeseq = raw_input("What is the native sequence? ")
seqfile = raw_input("What is the name of your sequences file? ")
path = raw_input("Where are your files? ~/Dropbox/Research/Structures/transcription_factor/lacI/")
path = "/Users/anumglasgow/Dropbox/Research/Structures/transcription_factor/lacI/" + path + "/" + seqfile

numres = len(nativeseq)

seqIDs = []
sequences = []

for seq_record in SeqIO.parse(path, "fasta"):
    seqIDs.append(seq_record.id)
    sequences.append(str(seq_record.seq))


temp = 0

for m in range(0, numres):
    
    res_dict = {"G":0, "A":0, "L":0, "M":0, "F":0, "W":0, "K":0, "Q":0, "E":0, "S":0, "P":0, "V":0, "I":0, "C":0, "Y":0, "H":0, "R":0, "N":0, "D":0, "T":0}
    
    residues = []
    for n in range(0, len(sequences)):
        residues.append(sequences[n][m])

        for k, v in res_dict.iteritems():
            for n in range(1, len(residues) + 1):
                if k == residues[n - 1]:
                    temp += 1
            res_dict[k] = temp
            temp = 0

    plt.bar(range(len(res_dict)), res_dict.values(), align = 'center')
    plt.xticks(range(len(res_dict)), list(res_dict.keys()))
    plt.title("Residue #" + str(m+1) + ": " + nativeseq[m])
    plt.ylabel("Frequency")
    plt.xlabel("Designed residue")

    plt.show()

