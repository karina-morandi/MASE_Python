import tkinter as tk
from tkinter import font
from tkinter import *
from ABFrame_Obj import ABFrame
from M29Frame_Obj import M29Frame
from WhirlPoolFrame_Obj import WhirlpoolFrame



class AppGUI(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.master = master
        self.master.title("Data Analysis & Visualisation")

        # This section creates the plot frame
        self.ABFrameObj = ABFrame(self)
        self.ABFrameObj.withdraw()

        self.M29FrameObj = M29Frame(self)
        self.M29FrameObj.withdraw()

        self.WhirlPoolFrameObj = WhirlpoolFrame(self)
        self.WhirlPoolFrameObj.withdraw()

        self.font_1 = font.Font(family="Calibri", size=16, weight="normal")
        self.font_2 = font.Font(family="Calibri", size=12, weight="normal")

        # Textvariables for the values specified by the user

        self.l1 = (tk.Label(master, text="Celestial Objects", font=self.font_1))
        self.l1.grid(row=0, column=0, columnspan=2, sticky=tk.N + tk.S + tk.E + tk.W)

        self.AB85_button = tk.Button(master, text="Abel 85", command=self.showAbel85, font=self.font_2)
        self.AB85_button.grid(row=1, column=1, sticky=N + S + E + W)

        self.M29_button = tk.Button(master, text="Pe M2-9", command=self.showM29, font=self.font_2)
        self.M29_button.grid(row=1, column=0, sticky=N + S + E + W)

        self.Whirlpool_button = tk.Button(master, text="Whirlpool", command=self.showWhirlPool, font=self.font_2)
        self.Whirlpool_button.grid(row=2, column=0, columnspan=2, sticky=N + S + E + W)

        self.close_button = (tk.Button(master, text="Close", command=self.CloseApplication, font=self.font_2))
        self.close_button.grid(row=3, column=0, columnspan=2, sticky=N + S + E + W)

    def showAbel85(self):
        self.ABFrameObj.show()
        self.master.withdraw()

    def showM29(self):
        self.M29FrameObj.show()
        self.master.withdraw()

    def showWhirlPool(self):
        self.WhirlPoolFrameObj.show()
        self.master.withdraw()

    def CloseApplication(self):
        print('closing')
        self.master.destroy()

    def show(self):
        self.master.update()
        self.master.deiconify()
