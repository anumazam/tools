#!/usr/bin/python


# find the lowest energy sequence in .fasta files from coupled moves output.

from Bio import SeqIO
from os import listdir
import numpy as np

folder = "20170911"
    
print "///////////////////////////////////////////////////"

path = "/Users/anumglasgow/Dropbox/Research/Structures/transcription_factor/lacI/" + folder + "/"

from os.path import isfile, join
allfiles = [f for f in listdir(path) if isfile(join(path, f))]

fasta_files = []
suffix = ".fasta"
for i in range(0, len(allfiles)):
    if allfiles[i].endswith(suffix):
        fasta_files.append(allfiles[i])
    filename = "/Users/anumglasgow/Dropbox/Research/Structures/transcription_factor/lacI/" + folder + "/sequences_loop"

for i in range(0, len(fasta_files)):
    path = "/Users/anumglasgow/Dropbox/Research/Structures/transcription_factor/lacI/" + folder + "/" + fasta_files[i]
    
    seqIDs = []
    sequences = []
    all_energies=[]
    
    for seq_record in SeqIO.parse(path, "fasta"):
        all_energies.append(seq_record.description.split()[1])
        seqIDs.append(seq_record.id)
        sequences.append(str(seq_record.seq))

    lowest_energy = np.amin(map(float, all_energies))

    target = open(filename, 'a')
    for i in [i for i,x in enumerate(map(float, all_energies)) if x == lowest_energy]:
        position = i
                
        print ">" + seqIDs[position]
        print sequences[position]
                
        target.write(">" + seqIDs[position] + "\n")
        target.write(sequences[position] + "\n")
    target.close()