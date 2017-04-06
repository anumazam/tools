#!/usr/bin/python

# this script runs compare_pt_mutants.py to find what point mutations have been made by backrub in the MS2 dimer-trimer.

import sys, os
import shutil

from subprocess import call
import shlex

chainID = ["A", "B", "C"]

for i in range(3):
    for j in range(129):
        shellstring = "python /Users/anum/Dropbox/Research/Scripts/compare_pt_mutants.py 7msf_noH2O_noRNA.pdb " + "chain" + chainID[i] + "/" + "res" + str(j+1) + "/" + "7msf_noH2O_noRNA_0001_low.pdb"

        call(shlex.split(shellstring))