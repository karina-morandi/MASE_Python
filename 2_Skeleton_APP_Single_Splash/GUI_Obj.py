import tkinter as tk
from tkinter import font
from tkinter.ttk import Combobox
from tkinter import filedialog
import tkinter.messagebox
import tkinter.simpledialog
from tkinter import *
import pylab as plt


class AppGUI(tk.Tk):

    def __init__(self, master, title):
        self.master = master
        self.master.title(title)
        self.ComicF1 = font.Font(family="Comic Sans MS", size=16, weight="normal")
        self.ComicF2 = font.Font(family="Comic Sans MS", size=10, weight="normal")
        self.ComicF3 = font.Font(family="Comic Sans MS", size=12, weight="normal")

        # StringVars to store user input
        self.firstName = tk.StringVar()
        self.lastName = tk.StringVar()
        self.email = tk.StringVar()
        root = tk.Tk()

        # Text variables for the values specified by the user

        self.l1 = tk.Label(master, text="Basic Contact Registration", font=self.ComicF1).grid(row=0, column=0, columnspan=2, sticky=tk.N + tk.S + tk.E + tk.W)

        tk.Label(root, text="First Name", font=self.ComicF3).grid(row=1, column=0, sticky=tk.N + tk.S + tk.E + tk.W)
        tk.Entry(root, textvariable=self.firstName, font=self.ComicF3).grid(row=1, column=1, sticky=tk.W)

        tk.Label(root, text="Last Name", font=self.ComicF3).grid(row=2, column=0, sticky=tk.N + tk.S + tk.E + tk.W)
        tk.Entry(root, textvariable=self.lastName, font=self.ComicF3).grid(row=2, column=1, sticky=tk.W)

        tk.Label(root, text="Email", font=self.ComicF3).grid(row=3, column=0, sticky=tk.N + tk.S + tk.E + tk.W)
        tk.Entry(root, textvariable=self.email, font=self.ComicF3).grid(row=3, column=1, sticky=tk.W)

        tk.Button(root, text="Register", font=self.ComicF3, command=self.Register).grid(row=4, column=0,
                                                                                        sticky=tk.N + tk.S + tk.E + tk.W)
        tk.Button(master, text="Close", command=self.CloseApplication, font=self.ComicF3).grid(row=17, column=0,
                                                                                               columnspan=2,
                                                                                               sticky=tk.N + tk.S + tk.E + tk.W)
    def Register(self):
        # Access user input using self.firstName.get(), self.lastName.get(), and self.email.get()
        print("First Name:", self.firstName.get())
        print("Last Name:", self.lastName.get())
        print("Email:", self.email.get())

    def CloseApplication(self):
        print('closing')
        self.master.destroy()
