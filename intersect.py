"""
intersect.py

Print the intersection and difference of two sets.
Use two csv files to start. One lists the names of the
companies in the DOW 30. The second lists companuies in
the NASDAQ 100

Peter Koppelman July 30, 2017
"""

import sys
import itertools
import csv

# Read in the two files from the harddrive
filename1 = "C:\\Users\\madan\\Downloads\\DowJones30.csv"
filename2 = "C:\\Users\\madan\\Downloads\\nasdaq100list.csv"

# test to make sure that the files are found and we have the permission
# to open them.
# First test the DowJones30 file.
try:
    dowjonescsv = open(filename1, encoding = "utf-8", newline = "")
except FileNotFoundError:
    print("Sorry, could not find file \"", filename1, "\".", sep = "")
    sys.exit(1)
except PermissionError:
    print("Sorry, no permission to open file \"", filename1, "\".", sep = "")
    sys.exit(1)

# Now try the Nasdaq 100 file.
try:
    nasdaq100csv = open(filename2, encoding = "utf-8", newline = "")
except FileNotFoundError:
    print("Sorry, could not find file \"", filename2, "\".", sep = "")
    sys.exit(1)
except PermissionError:
    print("Sorry, no permission to open file \"", filename2, "\".", sep = "")
    sys.exit(1)

dowjones = csv.reader((dowjonescsv), delimiter=';')
nasdaq100 = csv.reader(nasdaq100csv)

# Turn the files into sets.
# strip out any blanks and make the name of the company upper case for
# comparison later in the script.
dowjones = set([line[1].strip().upper() for line in dowjones])
nasdaq100 = set([line[1].strip().upper() for line in nasdaq100])

# create three files with companies in both indexes (intersection)
# companies just in the Dow Jones (dowjonesonly) and companies that
# are just in the Nasdaq 100.
intersection = dowjones & nasdaq100
dowjonesonly = dowjones - nasdaq100
nasdaq100only = nasdaq100 - dowjones

#Must specify fillvalue because the three sets are of different lengths.
threeColumns = itertools.zip_longest(
    sorted(dowjonesonly),
    sorted(intersection),
    sorted(nasdaq100only),
    fillvalue = ""
)

f = "{:22} {:22} {}"
print(f.format("Dow Jones Only", "     Both",        "Nasdaq 100 only"))
print(f.format("--------------", "----------------", "---------------"))

for left, middle, right in threeColumns:
    print(f.format(left.title(), middle.title(), right.title()))

sys.exit(0)


