#!/usr/bin/python
import random

# this is a tool for randomly assigning wells for 8 strains on a 96 well plate.

# create vectors for rows and columns
columns = []
for n in range(1, 13, 1):
    columns.append(n)

rowIDs = [ 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H' ]

# top half of the plate (+mev)
board = [1]*6 + [2]*6 + [3]*6 + [4]*6 +[5]*6 + [6]*6 +[7]*6 + [8]*6
random.shuffle(board)
board = [board[i:i + 12] for i in xrange(0, 48, 12)]

A = board[0]
B = board[1]
C = board[2]
D = board[3]

# bottom half of the plate (-mev)
board = [1]*6 + [2]*6 + [3]*6 + [4]*6 +[5]*6 + [6]*6 +[7]*6 + [8]*6
random.shuffle(board)
board = [board[i:i + 12] for i in xrange(0, 48, 12)]

E = board[0]
F = board[1]
G = board[2]
H = board[3]

# create table for plate
print "\n"
from tabulate import tabulate
print tabulate ([ A, B, C, D, E, F, G, H ], headers = columns, showindex = rowIDs, numalign = "center")

allrows = [ A, B, C, D, E, F, G, H ]

# print all locations for each strain

for strain in range (0, 8, 1):
    print "\n wells for strain #" + str(strain+1) + ":"
    
    for n in range(0, 8, 1):
        for i, j in enumerate(allrows[n]):
            if j == strain+1:
                print rowIDs[n] + str(i+1),

print "\n"

# export the table to an excel spreadsheet
import openpyxl
import datetime
import csv

today = datetime.date.today()
filename = str(today) + ".csv"

fl = open(filename, 'w')

writer = csv.writer(fl)
for values in allrows:
    writer.writerow(values)

fl.close()

#wb = openpyxl.Workbook()
#sheet = wb.active
#sheet.title = 'plate setup'
#
#wb.save(filename)






