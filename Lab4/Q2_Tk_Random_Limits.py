import random
import tkinter as tk
from tkinter import *
from tkinter import font
import tkinter.messagebox

root = tk.Tk()
root.title("Random Number Generator")
myfont1 = font.Font(family="Calibri", size=16, weight="normal")
myfont2 = font.Font(family="Calibri", size=14, weight="normal")
randVar = IntVar()

lowerRange = StringVar()
lowerRange.set(1)
upperRange = StringVar()
upperRange.set(100)


def GenerateRandomNumber(lw, hg):
    if lw > hg:
        tkinter.messagebox.showinfo("Inversion of values",
                                    "Careful, the lower range must be a lower integer value than the upper range "
                                    "value \nI have swapped them round for you")
        lowerRange.set("" + str(hg))
        upperRange.set("" + str(lw))
        return random.randint(int(hg), int(lw))
    else:
        return random.randint(lw, hg)


def main():
    randVar.set(GenerateRandomNumber(1,100))
    # Code to add widgets will go here...
    # Title label for the GUI
    l1 = tk.Label(root, text="Random Number Generator", font=myfont1)
    l1.grid(row=0, column=0, columnspan=2, sticky=tk.N + tk.S + tk.E + tk.W)

    # Label, entry pair
    # Random Number
    l2 = tk.Label(root, text="Random Number:", font=myfont2)
    l2.grid(row=1, column=0, sticky=tk.N + tk.S + tk.E + tk.W)
    e1 = tk.Entry(root, textvariable=randVar, font=myfont2)
    e1.grid(row=1, column=1, sticky=tk.W)
    e1.configure(state="disabled")

    # Lower Range
    l3 = tk.Label(root, text="Lower Range:", font=myfont2)
    l3.grid(row=2, column=0, sticky=tk.N + tk.S + tk.E + tk.W)
    e2 = tk.Entry(root, textvariable=lowerRange, font=myfont2)
    e2.grid(row=2, column=1, sticky=tk.W)

    # Upper Range
    l4 = tk.Label(root, text="Upper Range:", font=myfont2)
    l4.grid(row=3, column=0, sticky=tk.N + tk.S + tk.E + tk.W)
    e3 = tk.Entry(root, textvariable=upperRange, font=myfont2)
    e3.grid(row=3, column=1, sticky=tk.W)

    # Buttons to generate a new random or close application
    newRand = tk.Button(root, text="Generate New", font=myfont2, command=newRandNum)
    newRand.grid(row=4, column=0, sticky=tk.N + tk.S + tk.E + tk.W)
    closeApp = tk.Button(root, text="Close App", font=myfont2, command=CloseApplication)
    closeApp.grid(row=4, column=1, sticky=tk.N + tk.S + tk.E + tk.W)

    root.mainloop()


def newRandNum():
    lower = checkNumeric(lowerRange.get())
    upper = checkNumeric(upperRange.get())

    # Check if lower is less than or equal to upper
    if all([lower, upper]) == False:
        tkinter.messagebox.showwarning("Something is wrong with the inputs, are they numeric?")
    else:
        randVar.set(GenerateRandomNumber(int(lowerRange.get()), int(upperRange.get())))


def Convert2Numeric(val):
    return int(val)


def checkNumeric(val):
    # Check if both lower and upper ranges are valid integers
    try:
        val = int(val)
        return val
    except ValueError:
        tkinter.messagebox.showwarning("Ooopsie", "Something went wrong with this entry: " + val +
                                       "\nIt doesn't seem to be an integer")


def CloseApplication():
    print("closing")
    root.destroy()


if __name__ == "__main__":
    main()
