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

# numbers = [
#     ["0", []],
#     ["1", ["one", "unos", "un", "uno"]],
#     ["2", ["two", "dos", "deux", "due"]],
#     ["3", ["three", "tres", "trois", "tre"]],
#     ["4", ["four", "cuatro", "quatre", "quatro"]],
#     ["5", ["five", "cinco", "cinq", "cinque"]],
#     ["6", ["six", "seis", "six", "sei"]],
#     ["7", ["seven", "siete", "sept", "sette"]],
#     ["8", ["eight", "ocho", "huit", "otto"]],
#     ["9", ["nine", "nueve", "neuf", "nove"]],
#     ["10", ["ten", "diez", "dix", "dieci"]],
#      ]

numbers = [
    ["0", " ", " ", " ", " "],
    ["1", "one", "unos", "un", "uno"],
    ["2", "two", "dos", "deux", "due"],
    ["3", "three", "tres", "trois", "tre"],
    ["4", "four", "cuatro", "quatre", "quatro"],
    ["5", "five", "cinco", "cinq", "cinque"],
    ["6", "six", "seis", "six", "sei"],
    ["7", "seven", "siete", "sept", "sette"],
    ["8", "eight", "ocho", "huit", "otto"],
    ["9", "nine", "nueve", "neuf", "nove"],
    ["10", "ten", "diez", "dix", "dieci"],
     ]
Languages = ("English", "Spanish", "French", "Italian")


def buttonPress():   #Called when the button is pressed.
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

    
    # Lname is the index number of the language. I.e. English = 0, Spanish = 1, etc.
    Lname = int(languageNames.index(LanguageName.get()))
    
    print("Number =", Number)
    print("Lname = ", Lname + 1)
    # word = print(str(numbers[Number][Lname + 1]))
    word = print(numbers[Number][Lname + 1])
    # print(len(word))

    # sys.exit(0)
    # answerText.insert("1.0", word)
    answerText.insert("1.0", str(word))


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

#Make a list of the names of the languages.
languageNames = []   #Start with an empty list.
for language in Languages:
    languageNames.append(language)

LanguageName = tkinter.StringVar(root)
LanguageName.set(Languages[0])          #Menu displays this default choice.
LanguageMenu = tkinter.OptionMenu(root, LanguageName, *languageNames)
LanguageMenu.grid(row = 1, column = 1)

button = tkinter.Button(root, text = "Go", command = buttonPress)
button.grid(row = 1, column = 2)

# Anser text is the word that describes the number in the language that the user chose.
answerText = tkinter.Text(root, width = 45,
    height = 1, borderwidth = 2, relief = "groove")
answerText.grid(row = 2, column = 0, columnspan = 3)

root.mainloop()
