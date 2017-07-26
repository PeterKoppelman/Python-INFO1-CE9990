"""
do2.py

Demonstrate a tuple and the next command.
The advantage of the next command is that unlike a for loop it
stop the iteration as soon as it finds a match.
"""

import sys

# try this making notes a tuple
notes = [
    ("do", "deer, a female deer"),
    ("re", "drop of golden sun"),
    ("me", "name I call myself"),
    ("fa", "long, long way to run"),
    ("so", "needle pulling thread"),
    ("la", "note to follow so"),
    ("ti", "drink with jam and bread")
]

while True:
    try:
        note = input("Please type a note (e.g., do): ")
    except EOFError:
        sys.exit(0)

    try:
        verbiage = next(x for x in notes if x[0] == note)[1]
        print(note.capitalize(), ", a ", verbiage, ".", sep = "")
                
    except StopIteration:
        print("Sorry, \"", note, "\" is not a note.", sep = "")
        print()
        continue   #Go back up to the word "while".
    
    # print(note.capitalize(), ", a ", definition, ".", sep = "")
    print()
