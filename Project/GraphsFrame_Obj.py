import textwrap
import tkinter as tk
from tkinter import font
from tkinter import ttk
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image, ImageTk
import seaborn as sns
from sklearn.linear_model import LinearRegression
import csv


class GraphsFrame(tk.Toplevel):

    def __init__(self, master):
        tk.Toplevel.__init__(self, master)
        self.title("Data Visualization")
        self.protocol('WM_DELETE_WINDOW', self.OverrideWindow)

        self.plot_container = None

        data = pd.read_csv("world_population.csv")
        df = pd.DataFrame(data)

        self.ComicF1 = font.Font(family="Calibri", size=16, weight="normal")
        self.ComicF2 = font.Font(family="Calibri", size=12, weight="normal")

        buttonPanel = tk.Frame(self, background="black")
        buttonPanel.pack(side="left", fill="y")

        countries = df['Country/Territory'].unique()
        self.country_var = tk.StringVar()
        country_options = {country: country.replace(" ", "_") for country in countries}
        self.country_dropdown = ttk.Combobox(buttonPanel, textvariable=self.country_var,
                                             values=list(country_options.keys()))
        self.country_dropdown.grid(row=4, column=0, columnspan=2)
        self.country_dropdown.current(None)

        columns_list = ["2022 Population", "2020 Population", "2015 Population", "2010 Population", "2000 Population",
                        "1990 Population", "1980 Population", "1970 Population"]

        self.column_var = tk.StringVar()
        column_dropdown = ttk.Combobox(buttonPanel, textvariable=self.column_var, values=columns_list)
        column_dropdown.grid(row=2, column=0, columnspan=2)
        column_dropdown.current(None)

        self.updateButton = tk.Button(buttonPanel, text="Bins", command=self.binning, font=self.ComicF2, width=20)
        self.updateButton.grid(row=3, column=0, columnspan=4, pady=5)

        self.log = tk.Text(self, state='normal', height=20, width=60)
        self.log.pack(side="left", fill="both", expand=True)

        self.scrollB = tk.Scrollbar(self, command=self.log.yview)
        self.scrollB.pack(side="right", fill="y")

        self.basicButton = tk.Button(buttonPanel, text="Linear Regression", command=self.create_linear_regression_plot,
                                     font=self.ComicF2, width=20)
        self.basicButton.grid(row=6, column=0, columnspan=2, pady=5)

        self.sort_continent_button = tk.Button(buttonPanel, text="Correlations", command=self.correlation,
                                               font=self.ComicF2, width=20)
        self.sort_continent_button.grid(row=7, column=0, columnspan=2, pady=5)

        self.sort_population_2022_button = tk.Button(buttonPanel, text="Data Analysis",
                                                     command=self.population_in_different_years, font=self.ComicF2,
                                                     width=20)
        self.sort_population_2022_button.grid(row=8, column=0, columnspan=2, pady=5)

        self.close_Frame = tk.Button(buttonPanel, text="Close", command=self.hide, font=self.ComicF2, width=20)
        self.close_Frame.grid(row=9, column=0, columnspan=2, pady=5)

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

    def binning(self):
        data = pd.read_csv("world_population.csv")
        df = pd.DataFrame(data)
        selected_column = self.column_var.get()

        if selected_column in df.columns:
            column_info = df[selected_column].astype(int)
            custom_bins = [0, 1000000, 10000000, 50000000, 100000000, column_info.max()]
            labels = ['Very Small', 'Small', 'Medium', 'Large', 'Very Large']

            df['Binned Population'] = pd.cut(column_info, bins=custom_bins, labels=labels, include_lowest=True)
            self.print_to_log(str(df[['Country/Territory', selected_column, 'Binned Population']]))

            bin_percentages = df['Binned Population'].value_counts(normalize=True) * 100

            plt.figure(figsize=(8, 6))
            plt.pie(bin_percentages, labels=bin_percentages.index, autopct='%1.1f%%', startangle=140)
            plt.title('Percentage of Population in Each Bin')
            plt.axis('equal')
            pie_img_path = 'pie_chart.png'
            plt.savefig(pie_img_path)
            plt.close()

            # Display the pie chart in the GUI
            pie_img = Image.open(pie_img_path)
            pie_img = pie_img.resize((400, 300), Image.BICUBIC)  # Resize the image if needed
            pie_img_tk = ImageTk.PhotoImage(pie_img)
            self.print_to_log('Pie Chart - Percentage of Population in Each Bin:')
            self.log.image_create('end', image=pie_img_tk)
            self.log.image = pie_img_tk

            unique_bins = df['Binned Population'].unique()
            print(unique_bins)

        else:
            self.info_label.config(text="Column not found")

    def create_linear_regression_plot(self):
        data = pd.read_csv("world_population.csv")
        df = pd.DataFrame(data)
        selected_country = self.country_var.get()

        country_data = df[df['Country/Territory'] == selected_country]

        selected_years = ["1970 Population", "1980 Population", "1990 Population", "2000 Population", "2010 Population",
                          "2015 Population", "2020 Population", "2022 Population"]

        population_data = country_data[selected_years].values.ravel()

        X = np.arange(len(selected_years)).reshape(-1, 1)
        y = population_data

        lr = LinearRegression()
        lr.fit(X, y)
        predictions = lr.predict(X)

        plt.figure(figsize=(8, 6))
        plt.scatter(X, y, color='blue', label='Actual Population')
        plt.plot(X, predictions, color='red', label='Linear Regression')
        plt.title(f'Linear Regression Analysis for {selected_country} Population')
        plt.xlabel('Years')
        plt.ylabel('Population')
        plt.legend()
        plt.show()

    def correlation(self):
        data = pd.read_csv("world_population.csv")
        df = pd.DataFrame(data)
        correlation = df[['Growth Rate', 'World Population Percentage']].corr()
        self.print_to_log(str(correlation))
        sns.pairplot(df, y_vars=['Growth Rate'], x_vars=['World Population Percentage'], diag_kind='kde')
        plt.gcf().suptitle('Pairplot Demo Title')
        plt.show()

        selected_country = self.country_var.get()
        country_data = df[df['Country/Territory'] == selected_country]

        correlation = country_data[['Growth Rate', 'World Population Percentage']].corr()
        self.print_to_log(str(correlation))

    def population_in_different_years(self):
        data = pd.read_csv("world_population.csv")
        df = pd.DataFrame(data)
        selected_country = self.country_var.get()
        country_data = df[df['Country/Territory'] == selected_country]

        selected_years = ["1970 Population", "1980 Population", "1990 Population", "2000 Population", "2010 Population",
                          "2015 Population", "2020 Population", "2022 Population"]

        population_data = country_data[selected_years]

        wrapped_labels = [textwrap.fill(label, 10) for label in selected_years]

        fig, ax = plt.subplots()
        population_data.T.plot(kind='line', ax=ax)
        plt.xlabel('Years')
        plt.ylabel('Population')
        plt.title(f'Population Trend in Different Years for {selected_country}')
        plt.legend(loc='upper left')

        plt.xticks(ticks=range(len(wrapped_labels)), labels=wrapped_labels, rotation=45, ha='right')
        plt.tight_layout()
        plt.show()
