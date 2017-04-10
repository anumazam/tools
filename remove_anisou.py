#!/usr/bin/python

# remove ANISOU lines from .pdb files

t = open("S9G10_chainB.pdb","r+")
d = t.readlines()
t.seek(0)

for line in d:
    if not line.startswith("ANISOU"):
        t.write(line)

t.truncate()
t.close()
