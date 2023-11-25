import tkinter as tk
from tkinter import font
import pandas as pd
from matplotlib import pyplot as plt
from tabulate import tabulate
from PIL import Image, ImageTk
import csv
import io
import sys


class TablesFrame(tk.Toplevel):

    def __init__(self, master):
        tk.Toplevel.__init__(self, master)
        self.title("Tables Information")
        self.protocol('WM_DELETE_WINDOW', self.OverrideWindow)

        self.ComicF1 = font.Font(family="Calibri", size=16, weight="normal")
        self.ComicF2 = font.Font(family="Calibri", size=12, weight="normal")

        buttonPanel = tk.Frame(self, background="black")
        buttonPanel.pack(side="left", fill="y")

        self.titleLabel = tk.Label(buttonPanel, text="Tables Window", font=self.ComicF1)
        self.titleLabel.pack()

        self.tableButton = tk.Button(buttonPanel, text="Table", command=self.read_csv_data, font=self.ComicF2, width=30)
        self.tableButton.pack(padx=5, pady=5)

        self.basicButton = tk.Button(buttonPanel, text="Basic Info", command=lambda: self.tables_frame_preformEDA("world_population.csv"), font=self.ComicF2, width=30)
        self.basicButton.pack(padx=5, pady=5)

        self.sort_continent_button = tk.Button(buttonPanel, text="Sort by Continent", command=self.sort_by_continent, font=self.ComicF2, width=30)
        self.sort_continent_button.pack(padx=5, pady=5)

        self.sort_population_2022_button = tk.Button(buttonPanel, text="Sort by Population 2022", command=self.sort_by_population_2022, font=self.ComicF2, width=30)
        self.sort_population_2022_button.pack(padx=5, pady=5)

        self.sort_world_population_percentage_button = tk.Button(buttonPanel, text="Sort by World Population Percentage", command=self.sort_by_world_population_percentage, font=self.ComicF2, width=30)
        self.sort_world_population_percentage_button.pack(padx=5, pady=5)

        self.close_Frame = tk.Button(buttonPanel, text="Close", command=self.hide, font=self.ComicF2, width=30)
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
        self.update()
        self.deiconify()

    def OverrideWindow(self):
        self.hide()

    def hide(self):
        self.withdraw()
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
        self.preformEDA(filename)

    def preformEDA(self, filename):
        data = pd.read_csv("world_population.csv")

        self.print_to_log("\n\n\n******************** {0} ********************".format(filename))
        self.print_to_log('\n\nPrint DataFrame Info for {0}'.format(filename))
        buffer = io.StringIO()
        sys.stdout = buffer
        data.info()
        sys.stdout = sys.__stdout__

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
        data = pd.read_csv("world_population.csv")
        sorted_data = data.sort_values(by='Continent')[['Country/Territory', 'Continent', '2022 Population']]
        self.print_to_log(str(sorted_data))

        country_counts = sorted_data['Continent'].value_counts()

        # Create a pie chart
        plt.figure(figsize=(8, 6))
        plt.pie(country_counts, labels=country_counts.index, autopct='%1.1f%%', startangle=140)
        plt.title('Number of Countries per Continent')
        plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

        pie_img_path = 'countinents_chart.png'
        plt.savefig(pie_img_path)
        plt.close()

        # Display the pie chart in the GUI
        pie_img = Image.open(pie_img_path)
        pie_img = pie_img.resize((400, 300), Image.BICUBIC)  # Resize the image if needed
        pie_img_tk = ImageTk.PhotoImage(pie_img)
        self.print_to_log('Countries per Continent')
        self.log.image_create('end', image=pie_img_tk)
        self.log.image = pie_img_tk

    def sort_by_population_2022(self):
        data = pd.read_csv("world_population.csv")
        sorted_data = data.nlargest(n=20, columns='2022 Population')[['Country/Territory', '2022 Population', 'World Population Percentage']]
        self.print_to_log(str(sorted_data))

    def sort_by_world_population_percentage(self):
        data = pd.read_csv("world_population.csv")
        sorted_data = data.nlargest(n=20, columns='World Population Percentage')[['Country/Territory', 'Continent', 'World Population Percentage']]
        self.print_to_log(str(sorted_data))

