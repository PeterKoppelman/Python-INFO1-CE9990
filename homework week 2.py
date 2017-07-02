
"""
graphpaper.py

this program creates a graph. Input items are rows, columns and the spaces between the rows and columns
"""

import sys

def getInt(prompt):

    """
    Let the user input an integer
    """

    assert isinstance(prompt, str)

    while True:

        try:
            s = input(prompt)
        except EOFError:
            sys.exit(1)
        except KeyboardInterrupt:
            print("Control-C pressed. Exiting script. Thank you.")
            sys.exit(1)
        
        # if user has pressed the enter key exit the program
        if not s:
            print("Thank you... exiting routine")
            sys.exit(0)
            
        try:
            i = int(s)
        except ValueError:
            print("I'm sorry,", s, "is not an integer")
            continue
                
        return i


while True:
  no_rows = getInt("How many rows of boxes: ")
  no_columns = getInt("How many columns of boxes: ")
  spaces_rows = getInt("How many rows of spaces are in each box: ")
  spaces_col = getInt("How many columns spaces are in each box: ")
  
  # Create the length of hte horizontal line. Put the "+" on the end to finish off the right hand side of the box
  horizontal_lines = no_columns * ("+" + spaces_col * "-") + "+"

  # calculate the number of vertical rows that we need. Print them out every time vert increments.
  # put the "|" on the end to finish off the right hand side of the box
  vertical_lines = no_columns * ("|" + spaces_col * " ") + "|"
    
  for i in range (no_rows):  
    print(horizontal_lines)
    
    for j in range(spaces_rows):
        print(vertical_lines)
        
  # print out the horizontal line again to finish off the bottom row.  
  print(horizontal_lines)

  sys.exit(0)
