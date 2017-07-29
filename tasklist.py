"""
tasklist.py

Print one copy the name of each running process, in alphabetical order.
"""

import sys
import os
import csv

#Create a child process and a pipe as a csv file
infile = os.popen("tasklist /FO csv")   
lines = infile.readlines()      #lines is a list of lines.

lines = [line.split(",") for line in lines]
lines = sorted(set([line[0] for line in lines]))

print("           Image Name")
print("    =========================")
      
for i, line in enumerate(lines, start = 1):
    print("{:3} {}".format(i, line[1:-1])) # [1:-1] strips out the quotes

sys.exit(0)
