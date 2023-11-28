import pandas as pd
import geopandas as gpd
from shapely.geometry import Point
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from tkinter import ttk


class MapsFrame(tk.Toplevel):

    def __init__(self, master):
        tk.Toplevel.__init__(self, master)
        self.title("Maps")
        self.protocol('WM_DELETE_WINDOW', self.OverrideWindow)

        self.buttonPanel = tk.Frame(self, background="black")
        self.buttonPanel.pack(side="top", fill="x")

        # Sample data with coordinates
        self.city_data = pd.read_csv('worldcities.csv')
        self.data = pd.read_csv("world_population.csv")
        self.df = pd.DataFrame(self.data)

        countries = self.df['Country/Territory'].unique()
        self.country_var = tk.StringVar()
        country_options = {country: country.replace(" ", "_") for country in countries}
        self.country_dropdown = ttk.Combobox(self.buttonPanel, textvariable=self.country_var,
                                             values=list(country_options.keys()))
        self.country_dropdown.pack()
        self.country_dropdown.bind("<<ComboboxSelected>>", self.plot_map)

        self.fig, self.ax = plt.subplots(figsize=(10, 8))

        self.figure = plt.figure(figsize=(10, 8))
        self.canvas = FigureCanvasTkAgg(self.fig, master=self)
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    def plot_map(self, event=None):
        selected_country = self.country_var.get()

        # Filter cities for the selected country
        country_cities = self.city_data[self.city_data['country'] == selected_country]

        # Sort cities by population and select top 10 cities
        top_cities = country_cities.nlargest(10, 'population')

        # Creating a GeoDataFrame for the top cities
        gdf = gpd.GeoDataFrame(top_cities, geometry=gpd.points_from_xy(top_cities['lng'], top_cities['lat']))

        # Filter the world GeoDataFrame to include the selected country
        world = gpd.read_file('/Users/karina/Documents/MASE/Semester 1/Data Analysis and Visualization/Project/ne_110m_admin_0_countries/ne_110m_admin_0_countries.shp')
        # Assuming the column containing country names is 'country_name'
        country_boundaries = world[world['ADMIN'] == selected_country]

        # Clear previous plot
        self.ax.clear()

        # Plot country boundaries
        if not country_boundaries.empty:
            country_boundaries.plot(ax=self.ax, edgecolor='black', facecolor='none')
            self.ax.axis('off')  # Turn off the axis for country boundaries

        # Plot city dots
        if not gdf.empty:
            gdf.plot(ax=self.ax, color='red', marker='o', markersize=50, alpha=0.5, edgecolor='black')
            for x, y, label in zip(gdf.geometry.x, gdf.geometry.y, gdf['city']):
                self.ax.text(x, y, label, fontsize=9)

        # Update the canvas
        self.canvas.draw()

    def show(self):
        self.update()
        self.deiconify()

    def OverrideWindow(self):
        self.hide()

    def hide(self):
        self.withdraw()
        self.master.show_main_window()
