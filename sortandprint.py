"""

sortandprint.py


This script uses a sorted function with and without a lambda.
It does some nice printing to...

Peter Koppelman July 19, 2017
"""

import sys
import csv
from operator import itemgetter

oldfile = "C:\\users\\madan\\DOHMH_New_York_City_Restaurant_Inspection_Results.csv"

try:
    infile = csv.reader(open(oldfile, encoding = "utf-8", newline = ""))
except FileNotFoundError:
    print("Sorry, could not find file \"", oldfile, "\".", sep = "")
    sys.exit(1)
except PermissionError:
    print("Sorry, no permission to open file \"", oldfile, "\".", sep = "")
    sys.exit(1)


# Sort infile by fields 0 and 8 (CAMIS and date) so that the reviews of each
# establishment are sorted in order of the earliest first
newfile = sorted(infile, key = itemgetter(0, 8))
# newfile = sorted(infile, key = lambda x: x[0], x[8])

# print some key items for the first few records in the new file.
i = 0
camis = None
for line in newfile:
    if i < 50: # stop after record 50. This is arbitrary.
        if camis != line[0]:
            # print "header information"
            print()
            print()
            print(line[0]," ", line[1]," ",line[3]," ",line [4]," ",line [2]," ",line [5], sep="") 
            camis = line[0]
            
        # print detailed information (date and write-up)
        print("\t", line[8], sep = "", end = " ")
        temp = line[11]

        j = 0
        x = " " # this is a blank space so that wrapping around in the print statement looks better
        while len(temp) > 0:
            if j == 0:
                print(temp[:130])
            else:
                print("\t", x * 11, temp[:130], sep = "")
            temp = temp[130:]
            j += 1
        
        i += 1

sys.exit(0)
