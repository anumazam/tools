#!/usr/bin/python

# find the lowest energy sequence in .fasta files from coupled moves output.

from Bio import SeqIO
from os import listdir
import numpy as np

loops = 7

for n in range(1, loops + 1):
    
    print "///////////////////////////////////////////////////"
    print "loop #" + str(n)

    path = "/Users/anumglasgow/Dropbox/Research/Structures/transcription_factor/lacI/20170504_CM_LacI_ONPF/loop" + str(n) + "/"

    from os.path import isfile, join
    allfiles = [f for f in listdir(path) if isfile(join(path, f))]

    fasta_files = []
    suffix = ".fasta"
    for i in range(0, len(allfiles)):
        if allfiles[i].endswith(suffix):
            fasta_files.append(allfiles[i])

    for i in range(0, len(fasta_files)):
        path = "/Users/anumglasgow/Dropbox/Research/Structures/transcription_factor/lacI/20170504_CM_LacI_ONPF/loop" + str(n) + "/" + fasta_files[i]

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
