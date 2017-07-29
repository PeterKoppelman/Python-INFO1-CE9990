"""
tasklist.py

Print one copy the name of each running process, in alphabetical order.
"""

import sys
import os

infile = os.popen("tasklist")   #Create a child process and a pipe
lines = infile.readlines()      #lines is a list of lines.
status = infile.close()

if status != None:              #status is supposed to be None.
    print("\"tasklist\" produced exit status", status)
    sys.exit(1)

lines = sorted(set(lines[3:]))
lines = [line.rstrip() for line in lines]       #Remove trailing newline.

print("    Image Name                     PID Session Name        Session#    Mem Usage")
print("    =========================   ====== ============        ========   ==========")

for i, line in enumerate(lines, start = 1):
    print("{:3} {}".format(i, line))

sys.exit(0)
