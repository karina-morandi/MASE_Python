import webbrowser
from tkinter import *
import tkinter as tk
from tkinter import font
import pandas as pd
from tabulate import tabulate
import csv

class TablesFrame(tk.Toplevel):

    def __init__(self, master):
        tk.Toplevel.__init__(self, master)  # Initialize superclass
        self.title("Tables Information")
        self.protocol('WM_DELETE_WINDOW', self.OverrideWindow)

        # Set up the fonts you want to use
        self.ComicF1 = font.Font(family="Calibri", size=16, weight="normal")
        self.ComicF2 = font.Font(family="Calibri", size=12, weight="normal")

        # Create two panels, one is for the buttons and the other is for the canvas (images)
        buttonPanel = tk.Frame(self, background="black")
        # canvasPanel = tk.Frame(self, background="black")
        # Set the positioning of the panels
        buttonPanel.pack(side="left", fill="y")
        # canvasPanel.pack(side="right", fill="both", expand=True)

        # ill in these two areas:
        self._layoutButtons(buttonPanel)
        # self._layoutCanvas(canvasPanel)
        self.resizable(False, False)


    def _layoutButtons(self, parent):

        self.titleLabel = tk.Label(parent, text="Tables Window", font=self.ComicF1)
        self.titleLabel.grid(row=0, column=0, sticky=N+S+E+W)

        self.tableButton=tk.Button(parent, text="Table", command=self.read_csv_data, font=self.ComicF2)
        self.tableButton.grid(row=1, column=0, sticky=N+S+E+W, padx=5, pady=5)

        self.basicButton = tk.Button(parent, text="Basic Info", command=lambda: self.tables_frame_preformEDA("world_population.csv"), font=self.ComicF2)
        self.basicButton.grid(row=2, column=0, sticky=N+S+E+W, padx=5, pady=5)

        self.sort_continent_button = tk.Button(parent, text="Sort by Continent", command=self.sort_by_continent, font=self.ComicF2)
        self.sort_continent_button.grid(row=3, column=0, sticky=N + S + E + W, padx=5, pady=5)

        # Button for sorting by Population in 2022
        self.sort_population_2022_button = tk.Button(parent, text="Sort by Population 2022", command=self.sort_by_population_2022, font=self.ComicF2)
        self.sort_population_2022_button.grid(row=4, column=0, sticky=N + S + E + W, padx=5, pady=5)

        # Button for sorting by World Population Percentage
        self.sort_world_population_percentage_button = tk.Button(parent, text="Sort by World Population Percentage",command=self.sort_by_world_population_percentage,
                                                                 font=self.ComicF2)
        self.sort_world_population_percentage_button.grid(row=5, column=0, sticky=N + S + E + W, padx=5, pady=5)

        self.close_Frame = tk.Button(parent, text="Close", command=self.hide, font=self.ComicF2)
        self.close_Frame.grid(row=6, column=0, sticky=N+S+E+W, padx=5, pady=5)

    def show(self):
        self.update()       # Update the window
        self.deiconify() #Displays the window, after using either the iconify or the withdraw methods.

    def OverrideWindow(self):
        self.hide() # Hide the window

    def hide(self):
        self.withdraw() #Removes the window from the screen, without destroying it.
        self.master.show()

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

    def tables_frame_preformEDA(self, filename):
        print("Calling tables_frame_preformEDA for:", filename)
        # You can place your preformEDA logic here or call the existing preformEDA method
        self.preformEDA(filename)  # Calls the preformEDA method passing filename as argument

    def preformEDA(self, filename):
        print("Performing EDA for:", filename)
        data = pd.read_csv(filename)  # Load CSV into a pandas DataFrame

        print("\n\n\n******************** {0} ********************".format(filename))
        print('\n\nPrint DataFrame Info for {0}'.format(filename))
        print(data.info())
        print('\n\nPrint Number of Unique Items in {0}'.format(filename))
        print(data.nunique())
        print('\n\nPrint Number of Unique Items in Each Column for {0}'.format(filename))
        for column in data.columns:
            print(f'Column: {column}\n{data[column].unique()}')

        print("\n\nTable: {0}".format(filename))
        print(tabulate(data.head(), headers='keys', tablefmt='pretty', showindex=True))
        print(tabulate(data.tail(), headers='keys', tablefmt='pretty', showindex=True))

    def sort_by_continent(self):
        data = pd.read_csv("world_population.csv")  # Load CSV into a DataFrame
        sorted_data = data.sort_values(by='Continent')[['Country/Territory', 'Continent', '2022 Population']]  # Sort by 'Continent' column
        print(sorted_data)  # Display the sorted data (you can modify this to display as needed)

    def sort_by_population_2022(self):
        data = pd.read_csv("world_population.csv")  # Load CSV into a DataFrame
        sorted_data = data.nlargest(n=20, columns='2022 Population')[['Country/Territory', '2022 Population', 'World Population Percentage']]  # Sort by 'Population 2022' column
        print(sorted_data)  # Display the sorted data (you can modify this to display as needed)

    def sort_by_world_population_percentage(self):
        data = pd.read_csv("world_population.csv")  # Load CSV into a DataFrame
        sorted_data = data.nlargest(n=20, columns='World Population Percentage')[['Country/Territory', 'Continent', 'World Population Percentage']]  # Sort by 'World Population Percentage' column
        print(sorted_data)  # Display the sorted data (you can modify this to display as needed)

