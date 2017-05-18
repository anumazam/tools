#!/usr/bin/python

# calculate percent enrichment for each residue for a position in a designed loop

from Bio import SeqIO

import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import pylab as plt

# get information about native sequence, CM output from find_lowest_energy.py and path
nativeseq = raw_input("What is the native sequence? ")
start_res = raw_input("What is the first residue number? ")
start_res_int = int(start_res)
seqfile = raw_input("What is the name of your sequences file? ")
path = raw_input("Where are your files? ~/Dropbox/Research/Structures/transcription_factor/lacI/")
path = "/Users/anumglasgow/Dropbox/Research/Structures/transcription_factor/lacI/" + path + "/" + seqfile

numres = len(nativeseq)

# read in + store FASTA strings
seqIDs = []
sequences = []

for seq_record in SeqIO.parse(path, "fasta"):
    seqIDs.append(seq_record.id)
    sequences.append(str(seq_record.seq))

# create graph of the correct size (need to make this variable)
fig, axs = plt.subplots(6, 2)
fig.subplots_adjust(hspace = 1, wspace = .1)
tick_spacing = 1
x_labels = [' ', ' ', 'A', 'C', 'E', 'D', 'G', 'F', 'I', 'H', 'K', 'M', 'L', 'N', 'Q', 'P', 'S', 'R', 'T', 'W', 'V', 'Y']
axs = axs.ravel()

# iterate through each residue at each position in each sequence and tally enrichment over the whole loop for each possible amino acid
temp = 0

for m in range(0, numres):
    # reset tally before each sequence
    res_dict = {"G":0, "A":0, "L":0, "M":0, "F":0, "W":0, "K":0, "Q":0, "E":0, "S":0, "P":0, "V":0, "I":0, "C":0, "Y":0, "H":0, "R":0, "N":0, "D":0, "T":0}
    
    # check each sequence
    residues = []
    for n in range(0, len(sequences)):
        residues.append(sequences[n][m])

        # check the same residue in each sequence & populate dictionary (res_dict)
        for k, v in res_dict.iteritems():
            for n in range(1, len(residues) + 1):
                if k == residues[n - 1]:
                    temp += 1
            res_dict[k] = temp
            temp = 0

# graphing each subplot
    axs[m].xaxis.set_major_locator(ticker.MultipleLocator(tick_spacing))
    axs[m].bar(range(len(res_dict)), res_dict.values(), align = 'center', color = 'black')
    axs[m].set_title("Residue #" + str(start_res_int + m) + ": " + nativeseq[m], size = 8, fontweight = 'bold')
    axs[m].set_xticklabels(x_labels)
    axs[m].set_ylim(0, 20)
    axs[m].tick_params(direction='out', length=2, labelsize = 8)

# delete the extra plot, add a title and graph + save
fig.delaxes(axs[11])
plt.suptitle('Residue enrichment for CM design, residues ' + start_res + '-' + str(len(nativeseq) - 1 + start_res_int) + ', ' + nativeseq)
fig.set_size_inches(8, 10)
plt.savefig(path + '_enrichment.png')