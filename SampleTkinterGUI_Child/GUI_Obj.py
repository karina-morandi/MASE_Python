
import tkinter as tk
from tkinter import font

import tkinter.messagebox
import tkinter.simpledialog

from OtherFrameObj import NewFrame


class AppGUI(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.master = master
        self.master.title("MASE Data Analysis & Visualisation")

        # This section creates the plot frame
        self.OtherFrameObj = NewFrame(self)
        self.OtherFrameObj.withdraw()

        self.ComicF1 = font.Font(family="Comic Sans MS", size=16, weight="normal")
        self.ComicF2 = font.Font(family="Comic Sans MS", size=12, weight="normal")

        # Textvariables for the values specified by the user
        self.userEntry = tk.StringVar()
        self.userEntry.set(' ')

        self.l1 = tk.Label(master, text="Sample Tinkter GUI", font=self.ComicF1, bg='#FFFFCC')
        self.l1.grid(row=0,column=0,columnspan=2, sticky=tk.N + tk.S + tk.E + tk.W)

        self.labelEnterSomething = tk.Label(master, text="Enter Something", font=self.ComicF2).grid(row=1, column=0, sticky=tk.W)
        self.entryUserEntry = tk.Entry(master, textvariable=self.userEntry, font=self.ComicF2)
        self.entryUserEntry.grid(row=1, column=1, sticky=tk.W)

        self.click_me_button = tk.Button(master, text="Click Me!", command=self.DisplayMSG, font=self.ComicF2)
        self.click_me_button.grid(row=2,column=0,sticky=tk.N + tk.S + tk.E + tk.W)
        self.click_open_button = tk.Button(master, text="Open Frame", command=self.ShowNewFrame, font=self.ComicF2)
        self.click_open_button.grid(row=2,column=1,sticky=tk.N + tk.S + tk.E + tk.W)
        self.close_button = tk.Button(master, text="Close", command=self.CloseApplication, font=self.ComicF2)
        self.close_button.grid(row=3,column=0, columnspan=2, sticky=tk.N + tk.S + tk.E + tk.W)


    def ShowNewFrame(self):
      self.OtherFrameObj.show()

    def DisplayMSG(self):
        tkinter.messagebox.showinfo("Hello, great you got it working","What you entered is: \n"+self.userEntry.get()+"\nclick OK to continue?")

    def CloseApplication(self):
        print('closing')
        self.master.destroy()

    def show(self):
        """"""
        self.master.update()
        self.master.deiconify()

