import webbrowser
from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image
from tkinter import font
from Tables_Window import tablesWindow


class MainWindow(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)  # Initialize superclass
        self.master = master
        self.master.title("Final Project Main Window")

        self.Tables_Window = tablesWindow(self)
        self.Tables_Window.withdraw()

        # Set up the fonts you want to use
        self.myFont1 = font.Font(family="Calibri", size=16, weight="normal")
        self.myFont2 = font.Font(family="Calibri", size=12, weight="normal")

        # Create two panels, one is for the buttons and the other is for the canvas (images)
        buttonPanel = tk.Frame(self, background="black")
        canvasPanel = tk.Frame(self, background="black")
        # Set the positioning of the panels
        buttonPanel.grid(row=0, column=0, sticky="nsew")
        canvasPanel.grid(row=0, column=1, rowspan=3, sticky="nsew")

        # fill in these two areas:
        # self._layoutCanvas(canvasPanel)
        self.master.resizable(False, False)

        self.titleLabel = tk.Label(master, text="Main Window", font=self.myFont1)
        self.titleLabel.grid(row=0, column=0, sticky=N + S + E + W)

        self.info = tk.Button(master, text="Tables", command=self.showTables, font=self.myFont2)
        self.info.grid(row=1, column=0, sticky=N + S + E + W, padx=5, pady=5)

        self.buyPrint = tk.Button(master, text="Graphs", command=self.openURL_Video, font=self.myFont2)
        self.buyPrint.grid(row=2, column=0, sticky=N + S + E + W, padx=5, pady=5)

        self.close_Frame = tk.Button(master, text="Images", command=self.hide, font=self.myFont2)
        self.close_Frame.grid(row=3, column=0, sticky=N + S + E + W, padx=5, pady=5)

        self.close_Frame = tk.Button(master, text="Close", command=self.hide, font=self.myFont2)
        self.close_Frame.grid(row=4, column=0, sticky=N + S + E + W, padx=5, pady=5)

        img_Path = '/Users/karina/PycharmProjects/MASE_Python/Project/worldMap.jpeg'
        self.image = ImageTk.PhotoImage(file=img_Path)
        width = self.image.width()
        height = self.image.height()
        self.canvas = tk.Canvas(master, height=height, width=width)
        self.canvas.grid(row=0, column=1, rowspan=height, sticky=E)
        self.canvas.create_image(0, 1, anchor='nw', image=self.image)

    def show(self):
        self.update()  # Update the window
        self.deiconify()  # Displays the window, after using either the iconify or the withdraw methods.

    def OverrideWindow(self):
        self.hide()  # Hide the window

    def hide(self):
        self.withdraw()  # Removes the window from the screen, without destroying it.
        self.root.show()

    def showTables(self):
        self.Tables_Window.show()
        self.master.withdraw()

    def openURL_Video(self):
        url_video = "https://www.youtube.com/watch?v=RWJEfXOiebU"
        webbrowser.open_new_tab(url_video)
