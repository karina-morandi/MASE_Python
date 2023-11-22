import tkinter as tk
import webbrowser
from tkinter import *
from PIL import ImageTk
from tkinter import font
import csv  # Import CSV module

class AppGUI(tk.Tk):
    def __init__(self, master, title):
        self.master = master
        self.master.title(title)

        left_frame = tk.Frame(master)
        left_frame.grid(row=1, column=0, sticky="nsew")

        right_frame = tk.Frame(master)
        right_frame.grid(row=1, column=4, sticky="nsew")

        master.grid_rowconfigure(1, weight=1)
        master.grid_columnconfigure(0, weight=1)
        master.grid_columnconfigure(1, weight=1)

        # Rest of your GUI setup code...

        # Create font instances
        self.ComicF1 = font.Font(family="Calibri", size=16, weight="normal")
        self.ComicF3 = font.Font(family="Calibri", size=12, weight="normal")

        # Main Window Label
        self.l1 = tk.Label(master, text="Main Window", font=self.ComicF1)
        self.l1.grid(row=0, column=0, columnspan=2, sticky=tk.N + tk.S + tk.E + tk.W)

        # Buttons
        self.info = tk.Button(left_frame, text="Tables", command=self.read_csv_data, font=self.ComicF3)
        self.info.grid(row=1, column=0, sticky=N + S + E + W, padx=5, pady=5)

        # Rest of your button setup...

        # Canvas and Image setup
        img_Path = '/Users/karina/PycharmProjects/MASE_Python/Project/worldMap.jpeg'
        self.image = ImageTk.PhotoImage(file=img_Path)
        # Rest of your canvas setup...

    # Method to read data from the CSV file
    def read_csv_data(self):
        data_list = self.readFromCsvFile("world_population.csv")
        for item in data_list:
            print(item)
        # Handle the data_list as required (e.g., display, process, etc.)

    # Function to read data from the CSV file and return as a list
    def readFromCsvFile(self, filename):
        data_list = []
        with open(filename, 'r') as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                data_list.append(row)
        return data_list

    # Rest of your methods...

# Create and run the GUI
if __name__ == "__main__":
    root = tk.Tk()
    app = AppGUI(root, "My Application")
    root.mainloop()
