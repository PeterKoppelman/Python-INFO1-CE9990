"""
tknumber.py

Input a number between 1 and 10 and choose a language
(English, Spanish, French and Italian) and the spelling of the
word for the number will appear.

Peter Koppelman July 22, 2017

"""

import sys
import tkinter

#List of numbers with their corresponding names in four different languages
numbers = (
    (None),
    ("one", "unos", "un", "uno"), #1
    ("two", "dos", "deux", "due"), #2
    ("three", "tres", "trois", "tre"), #3
    ("four", "cuatro", "quatre", "quatro"), #4
    ("five", "cinco", "cinq", "cinque"), #5
    ("six", "seis", "six", "sei"), #6
    ("seven", "siete", "sept", "sette"), #7
    ("eight", "ocho", "huit", "otto"), #8
    ("nine", "nueve", "neuf", "nove"), #9
    ("ten", "diez", "dix", "dieci"), #10
     )

# list of languages for the pull down menu
Languages = ("English", "Spanish", "French", "Italian")

#Called when the button is pressed.
def buttonPress():
    """
    Get the number and the language,
    and display the corresponding word in the Text widget.
    """

    #Delete everything from the start of the Text ("1.0")
    #to the end of the Text (tkinter.END).
    answerText.delete("1.0", tkinter.END)

    try:
        #numberEntry.get() is the string typed into the Entry.
        Number = int(numberEntry.get())
    except ValueError:
        answerText.insert("1.0", numberEntry.get() + " is not an integer")
        return

    if Number < 1 or Number > 10:
        answerText.insert("1.0", "Number must be between 1 and 10.")
        return
    
    # Lnumber is the index number of the language. i.e. English = 0,
    # Spanish = 1, etc.
    try:
        Lnumber = Languages.index(LanguageName.get())
    except ValueError:
        answerText.insert("1.0", LanguageName.get() + " is not a valid language")
        return
   
    word = numbers[Number][Lnumber]
    answerText.insert("1.0", word)


root = tkinter.Tk()
root.title("Numbers")
# needed to change 330 to 350 on a windows machine
root.geometry("350x80")

#root contains a grid of 3 rows and 3 columns.
numberLabel = tkinter.Label(root, text = "Number", width = 15)
numberLabel.grid(row = 0, column = 0)

numberLabel = tkinter.Label(root, text = "Language", width = 15)
numberLabel.grid(row = 0, column = 1)

numberEntry = tkinter.Entry(root, width = 8)
numberEntry.grid(row = 1, column = 0)

LanguageName = tkinter.StringVar(root)
LanguageName.set(Languages[0])          #Menu displays this default choice.
LanguageMenu = tkinter.OptionMenu(root, LanguageName, *Languages)
LanguageMenu.grid(row = 1, column = 1)

button = tkinter.Button(root, text = "Go", command = buttonPress)
button.grid(row = 1, column = 2)

# Anser text is the word that describes the number in the language that the user chose.
answerText = tkinter.Text(root, width = 45,
    height = 1, borderwidth = 2, relief = "groove")
answerText.grid(row = 2, column = 0, columnspan = 3)

root.mainloop()
