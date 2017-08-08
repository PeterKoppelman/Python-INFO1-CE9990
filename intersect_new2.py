"""
intersect_new2.py

Print the intersection and difference of two sets (list of companes in the Dow Jones
Industrial AVerage and the Nasdaq 100..

Create a dictionary with the ticker symbols as the key and the name of the companies as the
value. Then crate two sets, one with the call symbols of hte DJIA and one with the
call symbols of the Nasdaq 100.

Peter Koppelman August 6, 2017
"""

import sys
import itertools
import csv
import urllib.request
import io

# This function opens the files from the web.
def openfile(filename, outfile):
    try:
        newfile = urllib.request.urlopen(filename)
        s = newfile.read()
        try:
            s = s.decode("utf-8")
        except UnicodeError as unicodeError:
            print(unicodeError)
            sys.exit(1)
        outfile += io.StringIO(s)
    except urllib.error.URLError as error:
        print("urllib.error.URLError", error)
        sys.exit(1)

# This function skips the header in a csv file.
def skipheader(filename, outfile, headerlines):
    try:
        next(filename) * headerlines
        for row in filename:
            outfile.append(row)
    except StopIteration:
        pass

# Create a uniquelist of the companies in each list. There can be duplicate
# company names because some companies have muliple classes of stock
# (i.e. GOOG and GOOGL).
def uniquelist(input, output):
    for row in input:
        if Reference.get(row).title() not in output:
            output.append(Reference.get(row).title())
            

# Get the file names from the web and call openfile function.
url1 = "https://raw.githubusercontent.com/PeterKoppelman/Python-INFO1-CE9990/master/dowjones30.csv"
dowjonescsv = []
openfile(url1, dowjonescsv)

url2 = "https://raw.githubusercontent.com/PeterKoppelman/Python-INFO1-CE9990/master/nasdaq100list.csv"
nasdaq100csv = []
openfile(url2, nasdaq100csv)
    
# Create a reference dictionary from the symbol and name fields in each file
# This is dictionary comprehension.
RefDow = {row['Symbol']: row['Name'] for row in csv.DictReader(dowjonescsv, delimiter = ';')}
RefNasdaq = {row['Symbol']: row['Name'] for row in csv.DictReader(nasdaq100csv, ('Symbol', 'Name'))}

# Final reference dictionary combines both files.
Reference = {}
Reference.update(RefNasdaq)
Reference.update(RefDow)

# Create new csv files to be passed to the skipheader function.
dowjones = csv.reader(dowjonescsv, delimiter=';')
nasdaq100 = csv.reader(nasdaq100csv)

nasdaqNew = []
skipheader(nasdaq100, nasdaqNew, 1)
DowNew = []
skipheader(dowjones, DowNew, 1)

# Turn the files into sets. Strip out any blanks and make the Symbol of the company
# upper case for comparison later in the script.
dowjones = set([line[0].strip().upper() for line in DowNew])
nasdaq100 = set([line[0].strip().upper() for line in nasdaqNew])

# create three files with companies in both sets (intersection), companies that are just in
# the Dow Jones (dowjonesonly) and companies that are just in the Nasdaq 100 (nasdaq100only).
intersection = dowjones & nasdaq100
dowjonesonly = dowjones - nasdaq100
nasdaq100only = nasdaq100 - dowjones

# Create files with names of companies, not the ticker symbols.
Both = []
uniquelist(intersection, Both)

DowJonesName = []
uniquelist(dowjonesonly, DowJonesName)

NasdaqName = []
uniquelist(nasdaq100only, NasdaqName)

#Must specify fillvalue because the three sets are of different lengths.
threeColumns = itertools.zip_longest(
    sorted(DowJonesName),
    sorted(Both),
    sorted(NasdaqName),
    fillvalue = ""
)

f = "{:22} {:22} {}"
print(f.format("Dow Jones Only", "     Both",        " Nasdaq 100 only"))
print(f.format("--------------", "----------------", " ---------------"))

for left, middle, right in threeColumns:
    # Print out the names of the companies
    print(f.format(left, middle, right))

sys.exit(0)
