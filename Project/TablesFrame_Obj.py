from tkinter import *
import tkinter as tk
from tkinter import font
import pandas as pd
from tabulate import tabulate
import csv
import io
import sys


class TablesFrame(tk.Toplevel):

    def __init__(self, master):
        tk.Toplevel.__init__(self, master)  # Initialize superclass
        self.title("Tables Information")
        self.protocol('WM_DELETE_WINDOW', self.OverrideWindow)

        self.ComicF1 = font.Font(family="Calibri", size=16, weight="normal")
        self.ComicF2 = font.Font(family="Calibri", size=12, weight="normal")

        # Create two panels, one is for the buttons and the other is for the canvas (images)
        buttonPanel = tk.Frame(self, background="black")
        # canvasPanel = tk.Frame(self, background="black")
        # Set the positioning of the panels
        buttonPanel.pack(side="left", fill="y")
        # canvasPanel.pack(side="right", fill="both", expand=True)

        # # ill in these two areas:
        # self._layoutButtons(buttonPanel)
        # # self._layoutCanvas(canvasPanel)
        # self.resizable(False, False)

        # Layout buttons within the button panel using pack()
        self.titleLabel = tk.Label(buttonPanel, text="Tables Window", font=self.ComicF1)
        self.titleLabel.pack()

        self.tableButton = tk.Button(buttonPanel, text="Table", command=self.read_csv_data, font=self.ComicF2)
        self.tableButton.pack(padx=5, pady=5)

        self.basicButton = tk.Button(buttonPanel, text="Basic Info", command=lambda: self.tables_frame_preformEDA("world_population.csv"), font=self.ComicF2)
        self.basicButton.pack(padx=5, pady=5)

        self.sort_continent_button = tk.Button(buttonPanel, text="Sort by Continent", command=self.sort_by_continent, font=self.ComicF2)
        self.sort_continent_button.pack(padx=5, pady=5)

        # Button for sorting by Population in 2022
        self.sort_population_2022_button = tk.Button(buttonPanel, text="Sort by Population 2022", command=self.sort_by_population_2022, font=self.ComicF2)
        self.sort_population_2022_button.pack(padx=5, pady=5)

        # Button for sorting by World Population Percentage
        self.sort_world_population_percentage_button = tk.Button(buttonPanel, text="Sort by World Population Percentage", command=self.sort_by_world_population_percentage, font=self.ComicF2)
        self.sort_world_population_percentage_button.pack(padx=5, pady=5)

        self.close_Frame = tk.Button(buttonPanel, text="Close", command=self.hide, font=self.ComicF2)
        self.close_Frame.pack(padx=5, pady=5)

        # Define self.log
        self.log = tk.Text(self, state='normal', height=20, width=60)
        self.log.pack(side="left", fill="both", expand=True)

        self.scrollB = tk.Scrollbar(self, command=self.log.yview)
        self.scrollB.pack(side="right", fill="y")

    def print_to_log(self, message):
        self.log.configure(state='normal')
        self.log.insert('end', message + '\n')
        self.log.configure(state='disabled')
        self.log.yview('end')

    def show(self):
        self.update()       # Update the window
        self.deiconify() #Displays the window, after using either the iconify or the withdraw methods.

    def OverrideWindow(self):
        self.hide() # Hide the window

    def hide(self):
        self.withdraw()  # Remove the window from the screen, without destroying it.
        self.master.show_main_window()

    def read_csv_data(self):
        data_list = self.readFromCsvFile("world_population.csv")
        for item in data_list:
            self.print_to_log(str(item))

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
        data = pd.read_csv("world_population.csv")  # Load CSV into a pandas DataFrame

        self.print_to_log("\n\n\n******************** {0} ********************".format(filename))
        self.print_to_log('\n\nPrint DataFrame Info for {0}'.format(filename))
        # self.print_to_log(str(data.info()))
        buffer = io.StringIO()
        sys.stdout = buffer
        data.info()
        sys.stdout = sys.__stdout__  # Reset standard output

        # Get the captured output
        captured_output = buffer.getvalue()
        self.print_to_log(captured_output)

        self.print_to_log('\n\nPrint Number of Unique Items in {0}'.format(filename))
        self.print_to_log(str(data.nunique()))
        self.print_to_log('\n\nPrint Number of Unique Items in Each Column for {0}'.format(filename))
        for column in data.columns:
            self.print_to_log(f'Column: {column}\n{data[column].unique()}')

        self.print_to_log("\n\nTable: {0}".format(filename))
        self.print_to_log(str(data.describe()))
        self.print_to_log(tabulate(data.head(), headers='keys', tablefmt='pretty', showindex=True))
        self.print_to_log(tabulate(data.tail(), headers='keys', tablefmt='pretty', showindex=True))

    def sort_by_continent(self):
        data = pd.read_csv("world_population.csv")  # Load CSV into a DataFrame
        sorted_data = data.sort_values(by='Continent')[['Country/Territory', 'Continent', '2022 Population']]  # Sort by 'Continent' column
        self.print_to_log(str(sorted_data))  # Display the sorted data (you can modify this to display as needed)

    def sort_by_population_2022(self):
        data = pd.read_csv("world_population.csv")  # Load CSV into a DataFrame
        sorted_data = data.nlargest(n=20, columns='2022 Population')[['Country/Territory', '2022 Population', 'World Population Percentage']]  # Sort by 'Population 2022' column
        self.print_to_log(str(sorted_data))  # Display the sorted data (you can modify this to display as needed)

    def sort_by_world_population_percentage(self):
        data = pd.read_csv("world_population.csv")  # Load CSV into a DataFrame
        sorted_data = data.nlargest(n=20, columns='World Population Percentage')[['Country/Territory', 'Continent', 'World Population Percentage']]  # Sort by 'World Population Percentage' column
        self.print_to_log(str(sorted_data))  # Display the sorted data (you can modify this to display as needed)

