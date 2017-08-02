"""
intersectNew.py

Print the intersection and difference of two sets (list of companes in the Dow Jones
Industrial AVerage and the Nasdaq 100..

Create a dictionary with the ticker symbols as the key and the name of the companies as the
value. Then crate two sets, one with the call symbols of hte DJIA and one with the
call symbols of the Nasdaq 100.

Peter Koppelman August 2, 2017
"""

import sys
import itertools
import csv

# Read in the two files from the harddrive
filename1 = "C:\\Users\\madan\\Downloads\\DowJones30.csv"
filename2 = "C:\\Users\\madan\\Downloads\\nasdaq100list.csv"

# check to make sure that the files are found and we have the permission to open them.
# First test the DowJones30 file.
try:
    dowjonescsv = open(filename1, encoding = "utf-8", newline = "")
except FileNotFoundError:
    print("Sorry, could not find file \"", filename1, "\".", sep = "")
    sys.exit(1)
except PermissionError:
    print("Sorry, no permission to open file \"", filename1, "\".", sep = "")
    sys.exit(1)

# Now the Nasdaq 100 file.
try:
    nasdaq100csv = open(filename2, encoding = "utf-8", newline = "")
except FileNotFoundError:
    print("Sorry, could not find file \"", filename2, "\".", sep = "")
    sys.exit(1)
except PermissionError:
    print("Sorry, no permission to open file \"", filename2, "\".", sep = "")
    sys.exit(1)


# Create a reference dictionary from the symbol and name fields in each file
RefNasdaq = {row['Symbol']: row['Name'] for row in csv.DictReader(nasdaq100csv, ('Symbol', 'Name'))}
RefDow = {row['Symbol']: row['Name'] for row in csv.DictReader(dowjonescsv, delimiter = ';')}

# Final reference dictionary combines both files.
Reference = {}
Reference.update(RefNasdaq)
Reference.update(RefDow)

# Re-open the files. For some reason they were closed.
dowjonescsv = open(filename1, encoding = "utf-8", newline = "")
dowjones = csv.reader(dowjonescsv, delimiter=';')
nasdaq100csv = open(filename2, encoding = "utf-8", newline = "")
nasdaq100 = csv.reader(nasdaq100csv)

# create a new file to skip the header in the Nasdaq file.
nasdaqNew = []
try:
    next(nasdaq100)
    for row in nasdaq100:
        nasdaqNew.append(row)
except StopIteration:
    pass

# create a new file to skip the header in the Dow Jones file.
DowNew = []
try:
    next(dowjones)
    for row in dowjones:
        DowNew.append(row)
except StopIteration:
    pass

# Turn the files into sets. Strip out any blanks and make the Symbol of the company
# upper case for comparison later in the script.
dowjones = set([line[0].strip().upper() for line in DowNew])
nasdaq100 = set([line[0].strip().upper() for line in nasdaqNew])


# create three files with companies in both sets (intersection), companies that are just in
# the Dow Jones (dowjonesonly) and companies that are just in the Nasdaq 100 (nasdaq100only).
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
print(f.format("Dow Jones Only", "     Both",        " Nasdaq 100 only"))
print(f.format("--------------", "----------------", " ---------------"))

for left, middle, right in threeColumns:
    # use the Reference file to print out the name of the company, not the ticker
    # symbol
    print(f.format(Reference.get(left,"").title(), Reference.get(middle,"").title(),\
                   Reference.get(right,"").title()))
sys.exit(0)


