import tkinter as tk
import webbrowser
from tkinter import *
from PIL import ImageTk
from tkinter import font
from TablesFrame_Obj import TablesFrame
from ImagesFrame_Obj import ImagesFrame

class AppGUI(tk.Frame):
    def __init__(self, master, title):
        tk.Frame.__init__(self, master)

        self.master = master
        self.master.title("Final Project")

        self.TablesObj = TablesFrame(self)
        self.TablesObj.withdraw()

        self.ImagesObj = ImagesFrame(self)
        self.ImagesObj.withdraw()

        left_frame = tk.Frame(master)
        left_frame.grid(row=1, column=0, sticky="nsew")

        # Configure the grid to expand with the window
        master.grid_rowconfigure(1, weight=1)
        master.grid_columnconfigure(0, weight=1)
        master.grid_columnconfigure(1, weight=1)

        self.ComicF1 = font.Font(family="Calibri", size=16, weight="normal")
        self.ComicF3 = font.Font(family="Calibri", size=12, weight="normal")
        self.l1 = tk.Label(master, text="Main Window", font=self.ComicF1).grid(row=0,column=0,columnspan=2, sticky=tk.N + tk.S + tk.E + tk.W)

        self.info = tk.Button(left_frame, text="Tables", command=self.showTables, font=self.ComicF3)
        self.info.grid(row=1, column=0, sticky=N + S + E + W, padx=5, pady=5)

        self.buyPrint = tk.Button(left_frame, text="Graphs", command=self.showTables, font=self.ComicF3)
        self.buyPrint.grid(row=2, column=0, sticky=N + S + E + W, padx=5, pady=5)

        self.images = tk.Button(left_frame, text="Images", command=self.showImages, font=self.ComicF3)
        self.images.grid(row=3, column=0, sticky=N + S + E + W, padx=5, pady=5)

        self.close_Frame = tk.Button(left_frame, text="Close", command=self.CloseApplication, font=self.ComicF3)
        self.close_Frame.grid(row=4, column=0, sticky=N + S + E + W, padx=5, pady=5)

        img_Path = '/Users/karina/PycharmProjects/MASE_Python/Project/worldMap.jpeg'
        self.image = ImageTk.PhotoImage(file=img_Path)
        width = self.image.width()
        height = self.image.height()
        self.canvas = tk.Canvas(master, height=height, width=width)
        self.canvas.grid(row=0, column=1, rowspan=height, sticky=E)
        self.canvas.create_image(0, 1, anchor='nw', image=self.image)

    def show_main_window(self):
        self.update()  # Update the window
        self.show()
    def show(self):
        self.master.update()  # Update the window
        self.master.deiconify()  # Displays the window, after using either the iconify or the withdraw methods.

    def OverrideWindow(self):
        self.hide()  # Hide the window

    def hide(self):
        self.withdraw()  # Removes the window from the screen, without destroying it.
        self.root.show()

    def showTables(self):
        self.TablesObj.show()
        self.master.withdraw()

    def showImages(self):
        self.ImagesObj.show()
        self.master.withdraw()

    def CloseApplication(self):
        print('closing')
        self.master.destroy()
