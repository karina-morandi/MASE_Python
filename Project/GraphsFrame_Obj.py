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

        self.growthVsPercButton = tk.Button(buttonPanel, text="Growth Rate vs World Percentage",
                                            command=self.growthRateVsWorldPercentage, font=self.ComicF2, width=20)
        self.growthVsPercButton.grid(row=5, column=0, columnspan=2, pady=5)

        self.popTrendButton = tk.Button(buttonPanel, text="Population Trend", command=self.create_combined_plots,
                                        font=self.ComicF2, width=20)
        self.popTrendButton.grid(row=6, column=0, columnspan=2, pady=5)

        self.densityVsGrowthButton = tk.Button(buttonPanel, text="Density vs Growth",
                                               command=self.densityVsGrowthRate, font=self.ComicF2, width=20)
        self.densityVsGrowthButton.grid(row=7, column=0, columnspan=2, pady=5)

        self.areaVsDensityButton = tk.Button(buttonPanel, text="Area vs Density", command=self.areaVsPopDensity,
                                             font=self.ComicF2, width=20)
        self.areaVsDensityButton.grid(row=8, column=0, columnspan=2, pady=5)

        self.popComparisonButton = tk.Button(buttonPanel, text="Population Comparison", command=self.popAndRegression,
                                             font=self.ComicF2, width=20)
        self.popComparisonButton.grid(row=9, column=0, columnspan=2, pady=5)

        self.popPerContinentButton = tk.Button(buttonPanel, text="Pop Comparison per Continent",
                                               command=self.popPerContinent, font=self.ComicF2, width=20)
        self.popPerContinentButton.grid(row=10, column=0, columnspan=2, pady=5)

        self.close_Frame = tk.Button(buttonPanel, text="Close", command=self.hide, font=self.ComicF2, width=20)
        self.close_Frame.grid(row=11, column=0, columnspan=2, pady=5)

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

            if 'Continent' in df.columns:
                grouped = df.groupby(['Continent', 'Binned Population'], observed=False).size().unstack(fill_value=0)

                self.print_to_log('Number of cities in each bin category for each continent:')
                self.print_to_log(str(grouped))

            plt.figure(figsize=(8, 6))
            plt.pie(bin_percentages, labels=bin_percentages.index, autopct='%1.1f%%', startangle=140)
            plt.title('Percentage of Population in Each Bin')
            plt.axis('equal')
            pie_img_path = 'pie_chart.png'
            plt.savefig(pie_img_path)
            plt.close()

            pie_img = Image.open(pie_img_path)
            pie_img = pie_img.resize((800, 600), Image.BICUBIC)
            pie_img_tk = ImageTk.PhotoImage(pie_img)
            self.print_to_log('Pie Chart - Percentage of Population in Each Bin:')
            self.log.image_create('end', image=pie_img_tk)
            self.log.image = pie_img_tk

            unique_bins = df['Binned Population'].unique()
            print(unique_bins)

        else:
            self.info_label.config(text="Column not found")

    def create_combined_plots(self):
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

        wrapped_labels = [textwrap.fill(label, 10) for label in selected_years]

        fig, axs = plt.subplots(1, 2, figsize=(15, 6))

        axs[0].scatter(X, y, color='blue', label='Actual Population')
        axs[0].plot(X, predictions, color='red', label='Linear Regression')
        axs[0].set_title(f'Linear Regression Analysis for {selected_country} Population')
        axs[0].set_xlabel('Years')
        axs[0].set_ylabel('Population')
        axs[0].legend()

        population_data = country_data[selected_years]
        axs[1].plot(population_data.T)
        axs[1].set_xlabel('Years')
        axs[1].set_ylabel('Population')
        axs[1].set_title(f'Population Trend in Different Years for {selected_country}')
        axs[1].legend(selected_years, loc='upper left')

        axs[1].set_xticks(range(len(selected_years)))
        axs[1].set_xticklabels(wrapped_labels, rotation=45, ha='right')

        plt.tight_layout()
        plt.show()

    def growthRateVsWorldPercentage(self):
        data = pd.read_csv("world_population.csv")
        df = pd.DataFrame(data)
        filtered_data = df[(df['Growth Rate'] > 0.96) & (df['Growth Rate'] < 1.06) &
                           (df['World Population Percentage'] < 12.5)]
        correlation = df[['Growth Rate', 'World Population Percentage']].corr()
        self.print_to_log(str(correlation))
        sns.pairplot(filtered_data, y_vars=['Growth Rate'], x_vars=['World Population Percentage'], diag_kind='kde')
        plt.suptitle('Growth Rate vs World Population Percentage')
        plt.show()

        selected_country = self.country_var.get()
        country_filtered_data = filtered_data[filtered_data['Country/Territory'] == selected_country]
        country_correlation = country_filtered_data[['Growth Rate', 'World Population Percentage']].corr()
        self.print_to_log(str(country_correlation))

    def densityVsGrowthRate(self):
        data = pd.read_csv("world_population.csv")
        df = pd.DataFrame(data)
        correlation = df[['Growth Rate', 'Density (per km)']].corr()
        self.print_to_log(str(correlation))
        sns.pairplot(df, y_vars=['Growth Rate'], x_vars=['Density (per km)'], diag_kind='kde')
        plt.gcf().suptitle('Growth Rate vs Density (per km)')
        plt.show()

        selected_country = self.country_var.get()
        country_data = df[df['Country/Territory'] == selected_country]

        correlation = country_data[['Growth Rate', 'Density (per km)']].corr()
        self.print_to_log(str(correlation))

    def areaVsPopDensity(self):
        data = pd.read_csv("world_population.csv")
        df = pd.DataFrame(data)
        filtered_data = df[(df['Density (per km)'] < 1188.5926) & (df['Area (km)'] < 7692024)]
        correlation = df[['Density (per km)', 'Area (km)']].corr()
        self.print_to_log(str(correlation))
        sns.pairplot(data=filtered_data, y_vars=['Density (per km)'], x_vars=['Area (km)'], diag_kind='kde')
        plt.suptitle('Density (per km) vs Area (km)')
        plt.show()

    def popAndRegression(self):
        data = pd.read_csv("world_population.csv")
        df = pd.DataFrame(data)

        recent_years = ["2022 Population"]
        older_years = ["1970 Population"]

        plt.figure(figsize=(12, 6))

        for i, recent_year in enumerate(recent_years):
            for j, older_year in enumerate(older_years):
                plt.subplot(1, 2, i * len(older_years) + j + 1)
                sns.scatterplot(data=data, x=recent_year, y=older_year)
                plt.title(f"{recent_year} vs {older_year}")
                plt.xlabel(recent_year)
                plt.ylabel(older_year)

        recent_year_column = '2022 Population'
        older_year_column = '1970 Population'

        X = df[[older_year_column]]
        y = df[recent_year_column]

        regression_model = LinearRegression()
        regression_model.fit(X, y)

        predictions = regression_model.predict(X)

        plt.subplot(1, 2, 2)
        plt.scatter(X, y, color='blue', label='Actual Data')
        plt.plot(X, predictions, color='red', label='Regression Line')

        plt.title('Linear Regression: Recent vs. Older Population Counts')
        plt.xlabel('Older Year Population')
        plt.ylabel('Recent Year Population')
        plt.legend()
        plt.grid(True)

        plt.tight_layout()
        plt.show()

        coefficients = regression_model.coef_
        intercept = regression_model.intercept_

        self.print_to_log(f'Coefficient (Slope): {coefficients[0]:.2f}')
        self.print_to_log(f'Intercept: {intercept:.2f}')

    def popPerContinent(self):
        data = pd.read_csv("world_population.csv")
        df = pd.DataFrame(data)

        filtered_data = df[df['1970 Population'] < 557501301]

        fig, ax = plt.subplots(figsize=(10, 8))

        for continent, group_data in filtered_data.groupby('Continent'):
            recent_year_column = '2022 Population'
            older_year_column = '1970 Population'

            x = group_data[older_year_column]
            y = group_data[recent_year_column]

            ax.scatter(x, y, label=f'{continent}')

            regression_model = LinearRegression()
            regression_model.fit(x.values.reshape(-1, 1), y)
            predictions = regression_model.predict(x.values.reshape(-1, 1))

            ax.plot(x, predictions, label=f'LinReg {continent}', linestyle='dashed')

        ax.set_title('Population Scatterplot with Linear Regression by Continent (1970 Population < 557501301)')
        ax.set_xlabel(f'Population in {older_year_column}')
        ax.set_ylabel(f'Population in {recent_year_column}')
        ax.legend()

        plt.tight_layout()
        plt.show()
