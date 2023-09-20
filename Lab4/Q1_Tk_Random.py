import random
import tkinter as tk
from tkinter import *
from tkinter import font

root = tk.Tk()
root.title("TUS Midlands")
myfont1 = font.Font(family="Calibri", size=16, weight="normal")
myfont2 = font.Font(family="Calibri", size=14, weight="normal")
randVar = IntVar()


def GenerateRandomNumber():
    return random.randint(1, 100)


def main():
    # Code to add widgets will go here...
    # Title label for the GUI
    l1 = tk.Label(root, text="Random Number Generator", font=myfont1)
    l1.grid(row=0, column=0, columnspan=2, sticky=tk.N + tk.S + tk.E + tk.W)

    # Label, entry pair
    l2 = tk.Label(root, text="Random Number:", font=myfont2)
    l2.grid(row=1, column=0, sticky=tk.N + tk.S + tk.E + tk.W)
    e1 = tk.Entry(root, textvariable=randVar, font=myfont2)
    e1.grid(row=1, column=1, sticky=tk.W)
    e1.configure(state="disabled")

    # Buttons to generate a new random or close application
    newRand = tk.Button(root, text="Generate New", font=myfont2, command=newRandNum)
    newRand.grid(row=2, column=0, sticky=tk.N + tk.S + tk.E + tk.W)
    closeApp = tk.Button(root, text="Close App", font=myfont2, command=CloseApplication)
    closeApp.grid(row=2, column=1, sticky=tk.N + tk.S + tk.E + tk.W)

    randVar.set(GenerateRandomNumber())

    root.mainloop()

def newRandNum():
    randVar.set(GenerateRandomNumber())


def CloseApplication():
    print("closing")
    root.destroy()


if __name__ == "__main__":
    main()
