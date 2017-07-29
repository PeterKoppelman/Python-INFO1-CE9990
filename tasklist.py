"""
tasklist.py

Print one copy the name of each running process, in alphabetical order.
"""

import sys
import os
import csv

# tasklist ists all of the processes that are running.
# The format (/fo csv) outputs everything as a csv file.
# /nh strips out the header. We can use all lines of output.
infile = os.popen("tasklist /fo csv /nh")   

# windows does not give you a nmessage that tells you that the
# popen command was successful or not (i.e. the way that Linux or Mac
# gives you a status result of None). As long as you spell everything
# correctly it works.

lines = csv.reader(infile)

# lines = [line.split(",") for line in lines]
lines = sorted(set([line[0] for line in lines]))

print("           Image Name")
print("    =========================")
      
for i, line in enumerate(lines, start = 1):
#     # print("{:3} {}".format(i, line[1:-1])) # [1:-1] strips out the quotes
    print("{:3} {}".format(i, line)) 

infile.close()
sys.exit(0)

