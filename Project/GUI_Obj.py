import tkinter as tk
import webbrowser
from tkinter import *
from PIL import ImageTk
from tkinter import font
import csv

class AppGUI(tk.Tk):
    def __init__(self, master, title):
        self.master = master
        self.master.title(title)

        left_frame = tk.Frame(master)
        left_frame.grid(row=1, column=0, sticky="nsew")

        # Create a frame for the right side (connection information)
        right_frame = tk.Frame(master)
        right_frame.grid(row=1, column=4, sticky="nsew")

        # Configure the grid to expand with the window
        master.grid_rowconfigure(1, weight=1)
        master.grid_columnconfigure(0, weight=1)
        master.grid_columnconfigure(1, weight=1)

        self.ComicF1 = font.Font(family="Calibri", size=16, weight="normal")
        self.ComicF3 = font.Font(family="Calibri", size=12, weight="normal")
        self.l1 = tk.Label(master, text="Main Window", font=self.ComicF1).grid(row=0,column=0,columnspan=2, sticky=tk.N + tk.S + tk.E + tk.W)

        self.info = tk.Button(left_frame, text="Tables", command=self.read_csv_data, font=self.ComicF3)
        self.info.grid(row=1, column=0, sticky=N + S + E + W, padx=5, pady=5)

        self.buyPrint = tk.Button(left_frame, text="Graphs", command=self.openURL_Video, font=self.ComicF3)
        self.buyPrint.grid(row=2, column=0, sticky=N + S + E + W, padx=5, pady=5)

        self.close_Frame = tk.Button(left_frame, text="Images", command=self.hide, font=self.ComicF3)
        self.close_Frame.grid(row=3, column=0, sticky=N + S + E + W, padx=5, pady=5)

        self.close_Frame = tk.Button(left_frame, text="Close", command=self.CloseApplication, font=self.ComicF3)
        self.close_Frame.grid(row=4, column=0, sticky=N + S + E + W, padx=5, pady=5)

        img_Path = '/Users/karina/PycharmProjects/MASE_Python/Project/worldMap.jpeg'
        self.image = ImageTk.PhotoImage(file=img_Path)
        width = self.image.width()
        height = self.image.height()
        self.canvas = tk.Canvas(master, height=height, width=width)
        self.canvas.grid(row=0, column=1, rowspan=height, sticky=E)
        self.canvas.create_image(0, 1, anchor='nw', image=self.image)

    def read_csv_data(self):
        data_list = self.readFromCsvFile("world_population.csv")
        for item in data_list:
            print(item)

    def readFromCsvFile(self, filename):
        data_list = []
        with open(filename, 'r') as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                data_list.append(row)
        return data_list


    def VisualiseGender(self):
        # values, labels = self.relationalDB.visualiseClient()
        # print(values)
        self.relationalDB.visualiseClient()

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

    def CloseApplication(self):
        print('closing')
        self.master.destroy()
