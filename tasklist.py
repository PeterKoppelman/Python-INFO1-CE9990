"""
tasklist.py

Print one copy the name of each running process, in alphabetical order.
"""

import sys
import os
import csv

# tasklist lists all of the processes that are running.
# The /fo csv outputs everything as a csv file.
# /nh strips out the header.
infile = os.popen("tasklist /fo csv /nh")   
lines = csv.reader(infile)
lines = sorted(set([line[0] for line in lines]))

status = infile.close()
# Check status of operation. Success is None. failure is anything but None. 
if status != None:      
    # print("\"tasklist statement\" produced exit status", status)
    print("tasklist statement produced exit status", status)
    sys.exit(1)

print("           Image Name")
print("    =========================")
      
for i, line in enumerate(lines, start = 1):
    print("{:3} {}".format(i, line)) 

sys.exit(0)
