import tkinter as tk
from tkinter import font
from tkinter import ttk
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
import datacleaner
from datacleaner import autoclean
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error,r2_score
from tabulate import tabulate
import csv

class GraphsFrame(tk.Toplevel):

    def __init__(self, master):
        tk.Toplevel.__init__(self, master)  # Initialize superclass
        self.title("Data Visualization")
        self.protocol('WM_DELETE_WINDOW', self.OverrideWindow)

        self.plot_container = None

        data = pd.read_csv("world_population.csv")  # Load CSV into a pandas DataFrame
        df = pd.DataFrame(data)

        self.ComicF1 = font.Font(family="Calibri", size=16, weight="normal")
        self.ComicF2 = font.Font(family="Calibri", size=12, weight="normal")

        buttonPanel = tk.Frame(self, background="black")
        buttonPanel.pack(side="left", fill="y")

        countries = df['Country/Territory'].unique()
        self.country_var = tk.StringVar()
        country_options = {country: country.replace(" ", "_") for country in countries}
        self.country_dropdown = ttk.Combobox(buttonPanel, textvariable=self.country_var, values=list(country_options.keys()))
        self.country_dropdown.grid(row=4, column=0, columnspan=2)
        self.country_dropdown.current(0)  # Set default value
        # country_label = tk.Label(buttonPanel, text="Select Country:")
        # country_label.grid(row=5, column=0, columnspan=2)

        # Get column names from the DataFrame
        columns_list = ["2022 Population", "2020 Population", "2015 Population","2010 Population", "2000 Population", "1990 Population", "1980 Population", "1970 Population"]
        # Dropdown menu for selecting columns
        self.column_var = tk.StringVar()
        column_dropdown = ttk.Combobox(buttonPanel, textvariable=self.column_var, values=columns_list)
        column_dropdown.grid(row=2, column=0, columnspan=2)
        column_dropdown.current(None)  # Set default value
        # column_label = tk.Label(buttonPanel, text="Select year:")
        # column_label.grid(row=1, column=0, columnspan=2)

        self.updateButton = tk.Button(buttonPanel, text="Binning", command=self.updateInfo, font=self.ComicF2, width=20)
        self.updateButton.grid(row=3, column=0, columnspan=4, pady=5)

        self.log = tk.Text(self, state='normal', height=20, width=60)
        self.log.pack(side="left", fill="both", expand=True)

        self.scrollB = tk.Scrollbar(self, command=self.log.yview)
        self.scrollB.pack(side="right", fill="y")

        self.basicButton = tk.Button(buttonPanel, text="Linear Regression", command=self.create_linear_regression_plot, font=self.ComicF2, width=20)
        self.basicButton.grid(row=6, column=0, columnspan=2, pady=5)

        self.sort_continent_button = tk.Button(buttonPanel, text="Correlations", command=self.correlation, font=self.ComicF2, width=20)
        self.sort_continent_button.grid(row=7, column=0, columnspan=2, pady=5)

        self.sort_population_2022_button = tk.Button(buttonPanel, text="Predictions", command=self.sort_by_population_2022, font=self.ComicF2, width=20)
        self.sort_population_2022_button.grid(row=8, column=0, columnspan=2, pady=5)

        self.close_Frame = tk.Button(buttonPanel, text="Close", command=self.hide, font=self.ComicF2, width=20)
        self.close_Frame.grid(row=9, column=0, columnspan=2, pady=5)


    def print_to_log(self, message):
        self.log.configure(state='normal')
        self.log.insert('end', message + '\n')
        self.log.configure(state='disabled')
        self.log.yview('end')

    def show(self):
        self.update()  # Update the window
        self.deiconify()  # Displays the window, after using either the iconify or the withdraw methods.

    def OverrideWindow(self):
        self.hide()  # Hide the window

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

    def updateInfo(self):
        data = pd.read_csv("world_population.csv")
        df = pd.DataFrame(data)
        selected_column = self.column_var.get()
        if selected_column in df.columns:
            column_info = df[selected_column].tolist()
            num_bins = 5
            bins = np.linspace(min(column_info), max(column_info), num_bins)
            self.print_to_log(str(bins))
            self.print_to_log(str(column_info))
            # self.info_label.config(text=str(column_info))
        else:
            self.info_label.config(text="Column not found")

    def create_linear_regression_plot(self):
        data = pd.read_csv("world_population.csv")
        df = pd.DataFrame(data)
        selected_country = self.country_var.get()
        #
        # # Filter data for Ireland
        # ireland_data = df[df['Country/Territory'] == 'Ireland']

        country_data = df[df['Country/Territory'] == selected_country]

        # Extract population data for the specified years
        selected_years = ["1970 Population", "1980 Population", "1990 Population","2000 Population","2010 Population","2015 Population","2020 Population","2022 Population"]

        population_data = country_data[selected_years].values.ravel()

        # Prepare X and y for linear regression
        X = np.arange(len(selected_years)).reshape(-1, 1)  # Years as features
        y = population_data  # Population as target

        # Perform linear regression
        lr = LinearRegression()
        lr.fit(X, y)
        predictions = lr.predict(X)

        # Visualize the results
        plt.figure(figsize=(8, 6))
        plt.scatter(X, y, color='blue', label='Actual Population')
        plt.plot(X, predictions, color='red', label='Linear Regression')
        plt.title(f'Linear Regression Analysis for {selected_country} Population')
        plt.xlabel('Years')
        plt.ylabel('Population')
        plt.legend()
        plt.show()


    def correlation(self):
            data = pd.read_csv("world_population.csv")  # Load CSV into a DataFrame
            df = pd.DataFrame(data)
            correlation = df[['Growth Rate', 'World Population Percentage']].corr()
            self.print_to_log(str(correlation))
            sns.pairplot(df, y_vars=['Growth Rate'], x_vars=['World Population Percentage'], diag_kind='kde')
            plt.gcf().suptitle('Pairplot Demo Title')
            plt.show()

    def sort_by_population_2022(self):
        data = pd.read_csv("world_population.csv")  # Load CSV into a DataFrame
        sorted_data = data.nlargest(n=20, columns='2022 Population')[
        ['Country/Territory', '2022 Population', 'World Population Percentage']]  # Sort by 'Population 2022' column
        # self.print_to_log(str(sorted_data))  # Display the sorted data (you can modify this to display as needed)

    def sort_by_world_population_percentage(self):
        data = pd.read_csv("world_population.csv")  # Load CSV into a DataFrame
        sorted_data = data.nlargest(n=20, columns='World Population Percentage')[['Country/Territory', 'Continent',
        'World Population Percentage']]  # Sort by 'World Population Percentage' column
        self.print_to_log(str(sorted_data))  # Display the sorted data (you can modify this to display as needed)