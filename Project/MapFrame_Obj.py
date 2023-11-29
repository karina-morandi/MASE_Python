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

        city_data = pd.read_csv('worldcities.csv')
        data = pd.read_csv("world_population.csv")
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

    def plot_map(self, event=None):
        selected_country = self.country_var.get()

        if self.plot_container is not None:
            self.plot_container.get_tk_widget().destroy()
            plt.close(self.fig)

        city_data = pd.read_csv('worldcities.csv')
        data = pd.read_csv("world_population.csv")
        df = pd.DataFrame(data)

        # Filter cities for the selected country
        country_cities = city_data[city_data['country'] == selected_country]

        # Sort cities by population and select top 10 cities
        top_cities = country_cities.nlargest(10, 'population')

        # Creating a GeoDataFrame for the top cities
        gdf = gpd.GeoDataFrame(top_cities, geometry=gpd.points_from_xy(top_cities['lng'], top_cities['lat']))

        # Filter the world GeoDataFrame to include the selected country
        world = gpd.read_file('ne_110m_admin_0_countries/ne_110m_admin_0_countries.shp')
        # Assuming the column containing country names is 'country_name'
        country_boundaries = world[world['ADMIN'] == selected_country]

        self.fig, self.ax = plt.subplots(figsize=(10, 8))

        self.canvas = FigureCanvasTkAgg(self.fig, master=self)
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        # Clear previous plot
        self.ax.clear()

        self.ax.axis('off')

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

        self.plot_container = self.canvas

    def show(self):
        self.update()
        self.deiconify()

    def OverrideWindow(self):
        self.hide()

    def hide(self):
        self.withdraw()
        self.master.show_main_window()
