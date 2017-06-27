""" NYU-SPS-Summer-2017-Section-2-
Homework assignments for Python class

inout.py

Homework for the first week of our Python class
"""

import sys

while True:  
  try:
    age = input("How old are you: ")

  # if EOF or Ctrl-C exit the program...
  except EOFError:
    sys.exit(0)
  except KeyboardInterrupt:
    print("trapped control-c. Ending the script. Thank you.")
    sys.exit(1)
    
  # check to see if user has pressed the enter key
  if not age:
    print("Thank you for pressing the enter key... exiting script.")
    sys.exit(0)

  # if input item is not a float, print an error message
  try:
    actual_age = float(age)
  except ValueError:
    print ("Sorry", age, "is not a number. Please try again.")
    continue

  dog_years = actual_age * 7
  print("That's about ",dog_years, "in dog years.")
  
  print()
  print("Press the enter key to exit the script.")
