#!/usr/bin/python

# calculate final grades for algebra class.

import sys
import pandas as pd
import numpy as np

# make array with homework grades from csv
homework = []
homework_nopercent = []
df = pd.read_csv(sys.argv[1], skiprows=3, nrows=10)
homework_strings = df.ix[:,8].values

# get rid of percents
for i in range(len(homework_strings)):
    homework_nopercent.append(homework_strings[i].strip('%'))

homework = [float(numeric_string) for numeric_string in homework_nopercent]

# drop lowest grade
homework_sorted = sorted(homework)
homework_sorted = homework_sorted[1:10]

homework_avg = np.mean(homework_sorted)

# make array with quiz grades from csv
quiz = []
quiz_nopercent = []
df = pd.read_csv(sys.argv[1], skiprows=17, nrows=9)
quiz_strings = df.ix[:,8].values

# get rid of percents
for i in range(len(quiz_strings)):
    quiz_nopercent.append(quiz_strings[i].strip('%'))

quiz = [float(numeric_string) for numeric_string in quiz_nopercent]

# drop lowest two grades
quiz_sorted = sorted(quiz)
quiz_sorted = quiz_sorted[2:8]

quiz_avg = np.mean(quiz_sorted)

# get exam 1 grade
exam1 = []
exam1_nopercent = []
df = pd.read_csv(sys.argv[1], skiprows=30, nrows=1)
exam1_strings = df.ix[:,8].values

for i in range(len(exam1_strings)):
    exam1_nopercent.append(exam1_strings[i].strip('%'))

exam1 = [float(numeric_string) for numeric_string in exam1_nopercent]

exam1_avg = np.mean(exam1)

# get exam 2 grade
exam2 = []
exam2_nopercent = []
df = pd.read_csv(sys.argv[1], skiprows=35, nrows=1)
exam2_strings = df.ix[:,8].values

for i in range(len(exam2_strings)):
    exam2_nopercent.append(exam2_strings[i].strip('%'))

exam2 = [float(numeric_string) for numeric_string in exam2_nopercent]

exam2_avg = np.mean(exam2)

# get final grade
final = []
final_nopercent = []
df = pd.read_csv(sys.argv[1], skiprows=45, nrows=1)
final_strings = df.ix[:,8].values

for i in range(len(exam2_strings)):
    final_nopercent.append(final_strings[i].strip('%'))

final = [float(numeric_string) for numeric_string in final_nopercent]

final_avg = np.mean(final)

# get participation grade
participation = []
participation_nopercent = []
df = pd.read_csv(sys.argv[1], skiprows=40, nrows=1)
participation_strings = df.ix[:,8].values

for i in range(len(participation_strings)):
    participation_nopercent.append(participation_strings[i].strip('%'))

participation = [float(numeric_string) for numeric_string in participation_nopercent]

participation_avg = np.mean(participation)

# calculate final grade
print sys.argv[1]
print "homework avg " + str(homework_avg)
print "quiz avg " + str(quiz_avg)
print "exam 1 " + str(exam1_avg)
print "exam 2 " + str(exam2_avg)
print "final exam " + str(final_avg)
print "participation " + str(participation_avg)

if final_avg <= 60:
    print "letter grade: F"
    print "\n"

elif final_avg >60:
    final_grade = homework_avg * .15 + quiz_avg * .20 + exam1_avg * .15 + exam2_avg * .20 + final_avg * .25 + participation_avg * .05
    print "FINAL GRADE " + str(final_grade)

    if final_grade >= 90:
        print "letter grade: A"
    elif final_grade >= 80:
        print "letter grade: B"
    elif final_grade >= 70:
        print "letter grade: C"
    elif final_grade >= 60:
        print "letter grade: D"
    elif final_grade < 60:
        print "letter grade: F"

    print "\n"
