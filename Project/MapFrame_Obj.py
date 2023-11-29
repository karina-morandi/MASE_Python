import os
import sys
import pandas as pd
import geopandas as gpd
from tkinter import font
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from tkinter import ttk


class MapsFrame(tk.Toplevel):

    def __init__(self, master):
        tk.Toplevel.__init__(self, master)
        self.title("Maps")
        self.protocol('WM_DELETE_WINDOW', self.OverrideWindow)

        self.plot_container = None

        base_path = self.resource_path("")  # Get base path for bundled app

        city_data = pd.read_csv(os.path.join(base_path, 'worldcities.csv'))
        data = pd.read_csv(os.path.join(base_path, "world_population.csv"))
        df = pd.DataFrame(data)

        self.ComicF1 = font.Font(family="Calibri", size=16, weight="normal")

        buttonPanel = tk.Frame(self, background="black")
        buttonPanel.pack(side="top", fill="x")

        countries = df['Country/Territory'].unique()
        self.country_var = tk.StringVar()
        country_options = {country: country.replace(" ", "_") for country in countries}
        self.country_dropdown = ttk.Combobox(buttonPanel, textvariable=self.country_var,
                                             values=list(country_options.keys()))
        self.country_dropdown.grid(row=0, column=0, columnspan=2)
        self.country_dropdown.current(None)
        self.country_dropdown.bind("<<ComboboxSelected>>", self.plot_map)

    def resource_path(self, relative_path):
        """Get absolute path to resource, works for dev and for PyInstaller"""
        if hasattr(sys, '_MEIPASS'):
            return os.path.join(sys._MEIPASS, relative_path)
        return os.path.join(os.path.abspath("."), relative_path)


    def plot_map(self, event=None):
        selected_country = self.country_var.get()

        if self.plot_container is not None:
            self.plot_container.get_tk_widget().destroy()
            plt.close(self.fig)

        base_path = self.resource_path("")  # Get base path for bundled app

        csv_pop = "world_population.csv"
        file_path = self.resource_path(csv_pop)
        data = pd.read_csv(file_path)

        csv_city = "worldcities.csv"
        file_city = self.resource_path(csv_city)
        city_data = pd.read_csv(file_city)

        country_cities = city_data[city_data['country'] == selected_country]

        top_cities = country_cities.nlargest(10, 'population')

        gdf = gpd.GeoDataFrame(top_cities, geometry=gpd.points_from_xy(top_cities['lng'], top_cities['lat']))

        world_shp = 'ne_110m_admin_0_countries/ne_110m_admin_0_countries.shp'
        file_world = self.resource_path(world_shp)
        world = gpd.read_file(file_world, encoding='latin1')

        country_boundaries = world[world['ADMIN'] == selected_country]

        self.fig, self.ax = plt.subplots(figsize=(10, 8))

        self.canvas = FigureCanvasTkAgg(self.fig, master=self)
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        self.ax.clear()

        self.ax.axis('off')

        if not country_boundaries.empty:
            country_boundaries.plot(ax=self.ax, edgecolor='black', facecolor='none')
            self.ax.axis('off')

        if not gdf.empty:
            gdf.plot(ax=self.ax, color='red', marker='o', markersize=50, alpha=0.5, edgecolor='black')
            for x, y, label in zip(gdf.geometry.x, gdf.geometry.y, gdf['city']):
                self.ax.text(x, y, label, fontsize=9)

        self.canvas.draw()
        self.plot_container = self.canvas

    def show(self):
        self.update()
        self.deiconify()

    def OverrideWindow(self):
        self.hide()

    def hide(self):
        self.withdraw()
        self.master.show_main_window()
