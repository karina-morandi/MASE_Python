from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import font


class NewFrame(Toplevel):

    def __init__(self, master):
        super().__init__()  # Initialize superclass
        self.root = master
        """Constructor"""
        self.ComicF1 = font.Font(family="Comic Sans MS", size=16, weight="normal")
        self.ComicF2 = font.Font(family="Comic Sans MS", size=12, weight="normal")

        self.titleLabel = Label(self, text="A child frame", font=self.ComicF1)
        self.titleLabel.grid(row=0, column=0, columnspan=5, sticky=N + S + E + W)

        self.title("Plotting Options")
        self.protocol('WM_DELETE_WINDOW', self.OverrideWindow)
        self.geometry("710x480")

    def show(self):
        self.update()
        self.deiconify()

    def OverrideWindow(self):
        self.hide()

    def hide(self):
        self.withdraw()
        self.root.show()
