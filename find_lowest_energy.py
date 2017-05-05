#!/usr/bin/python

# find the lowest energy sequence in .fasta files from coupled moves output.

from Bio import SeqIO
import numpy as np

path = "/Users/anumglasgow/Dropbox/Research/Structures/transcription_factor/lacI/20170504_CM_LacI_ONPF/loop1/2p9h_ONPF_A_withH_noH2O_0001.fasta"

seqIDs = []
sequences = []
all_energies=[]

for seq_record in SeqIO.parse(path, "fasta"):
    all_energies.append(seq_record.description.split()[1])
    seqIDs.append(seq_record.id)
    sequences.append(str(seq_record.seq))

lowest_energy = np.amin(map(float, all_energies))

for i in [i for i,x in enumerate(map(float, all_energies)) if x == lowest_energy]:
    position = i

print ">" + seqIDs[position]
print sequences[position]
