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
lowerRange = StringVar(value="1")
upperRange = StringVar(value="100")


def GenerateRandomNumber():
    lower = lowerRange.get()
    upper = upperRange.get()

    # Check if both lower and upper ranges are valid integers
    try:
        lower = int(lower)
        upper = int(upper)
    except ValueError:
        tkinter.messagebox.showwarning("Error", "Invalid lower or upper range")
        return

    # Check if lower is less than or equal to upper
    if lower > upper:
        tkinter.messagebox.showerror("Error", "Lower range must be less than or equal to upper range.")
        return

    return random.randint(lower, upper)


def main():
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
    e2.configure(state="normal")

    # Upper Range
    l4 = tk.Label(root, text="Upper Range:", font=myfont2)
    l4.grid(row=3, column=0, sticky=tk.N + tk.S + tk.E + tk.W)
    e3 = tk.Entry(root, textvariable=upperRange, font=myfont2)
    e3.grid(row=3, column=1, sticky=tk.W)
    e3.configure(state="normal")

    # Buttons to generate a new random or close application
    newRand = tk.Button(root, text="Generate New", font=myfont2, command=newRandNum)
    newRand.grid(row=4, column=0, sticky=tk.N + tk.S + tk.E + tk.W)
    closeApp = tk.Button(root, text="Close App", font=myfont2, command=CloseApplication)
    closeApp.grid(row=4, column=1, sticky=tk.N + tk.S + tk.E + tk.W)

    randVar.set(GenerateRandomNumber())

    root.mainloop()


def newRandNum():
    randVar.set(GenerateRandomNumber())


def CloseApplication():
    print("closing")
    root.destroy()


if __name__ == "__main__":
    main()
