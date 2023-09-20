import tkinter as tk
from tkinter import font
from tkinter.ttk import Combobox
from tkinter import filedialog
import tkinter.messagebox
import tkinter.simpledialog
from tkinter import *
import pylab as plt
from ChildA_Obj import AFrame
from ChildB_Obj import BFrame


class AppGUI(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.master = master
        # self.master.title(aTitle)

        # This section creates the plot frame
        self.ChildA_Obj = AFrame(self)
        self.ChildA_Obj.withdraw()
        self.ChildB_Obj = BFrame(self)
        self.ChildB_Obj.withdraw()

        self.font_1 = font.Font(family="Calibri", size=16, weight="normal")
        self.font_2 = font.Font(family="Calibri", size=12, weight="normal")

        # Textvariables for the values specified by the user

        self.l1 = (tk.Label(master, text="Sample Parent Child", font=self.font_1))
        self.l1.grid(row=0, column=0, columnspan=2, sticky=tk.N + tk.S + tk.E + tk.W)

        self.childA_Button = tk.Button(master, text="Child A", command=self.showChildA, font=self.font_2)
        self.childA_Button.grid(row=1, column=0, sticky=tk.N + tk.S + tk.E + tk.W)
        self.childB_Button = tk.Button(master, text="Child B", command=self.showChildB, font=self.font_2)
        self.childB_Button.grid(row=1, column=1, sticky=tk.N + tk.S + tk.E + tk.W)

        self.close_button = (tk.Button(master, text="Close", command=self.CloseApplication, font=self.font_2))
        self.close_button.grid(row=2, column=0, columnspan=2, sticky=tk.N + tk.S + tk.E + tk.W)

    def showChildA(self):
        self.ChildA_Obj.show()
        self.master.withdraw()

    def showChildB(self):
        self.ChildB_Obj.show()
        self.master.withdraw()

    def CloseApplication(self):
        print('closing')
        self.master.destroy()

    def show(self):
        """"""
        self.master.update()
        self.master.deiconify()
