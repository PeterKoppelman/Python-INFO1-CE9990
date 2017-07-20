"""

opencsv.py

This code test the csv reader and csv writer to see if you can use a delimiter
other than a comma.

Peter Koppelman July 19, 2017
"""

import sys
import csv

oldfile = "C:\\users\\madan\\DOHMH_New_York_City_Restaurant_Inspection_Results.csv"

try:
    infile = csv.reader(open(oldfile, encoding = "utf-8", newline = ""))
except FileNotFoundError:
    print("Sorry, could not find file \"", oldfile, "\".", sep = "")
    sys.exit(1)
except PermissionError:
    print("Sorry, no permission to open file \"", oldfile, "\".", sep = "")
    sys.exit(1)

# the following code uses csv.writer to create a csv file with a tilda (~) as
# a delimiter.
outfile = open("C:\\users\\madan\\temp.csv", "w")
writer = csv.writer(outfile, delimiter='~', quotechar='|', quoting=csv.QUOTE_MINIMAL)

for row in infile:
    writer.writerow(row)

outfile.close()

sys.exit(0)
