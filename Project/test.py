import pandas as pd
import geopandas as gpd
from shapely.geometry import Point
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from tkinter import ttk

class Test:

    def __init__(self, master):
        self.master = master
        self.master.title("Data Visualization")

        self.buttonPanel = tk.Frame(self.master, background="black")
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

        self.figure = plt.figure(figsize=(16, 8))  # Adjust the figure size to accommodate side-by-side maps
        self.canvas = FigureCanvasTkAgg(self.figure, master=self.master)
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    def plot_map(self, event=None):
        selected_country = self.country_var.get()

        # Filter cities for the selected country
        country_cities = self.city_data[self.city_data['country'] == selected_country]

        # Sort cities by population and select top 10 cities
        top_cities = country_cities.nlargest(10, 'population')

        # Creating a GeoDataFrame for the top cities
        gdf = gpd.GeoDataFrame(top_cities, geometry=[Point(xy) for xy in zip(top_cities['lng'], top_cities['lat'])])

        # Filter the world GeoDataFrame to include the selected country
        world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
        country_boundaries = world[world['name'] == selected_country]

        # Clear previous plots
        self.figure.clear()

        # Plotting the data for the selected country in two subplots
        ax1 = self.figure.add_subplot(121)
        ax1.axis('off')  # Turn off the axis
        ax2 = self.figure.add_subplot(122)
        ax2.axis('off')  # Turn off the axis

        # Plot country boundaries in the first subplot
        if not country_boundaries.empty:
            country_boundaries.plot(ax=ax1, edgecolor='black', facecolor='none')
            ax1.set_title('Country Boundaries')

        # Plot city dots in the second subplot
        if not gdf.empty:
            country_boundaries.plot(ax=ax2, edgecolor='black', facecolor='none')  # Plot country boundaries first
            gdf.plot(ax=ax2, color='red', marker='o', markersize=50, alpha=0.5, edgecolor='black')
            ax2.set_title('Top 10 Cities')

            for x, y, label in zip(gdf.geometry.x, gdf.geometry.y, gdf['city']):
                ax2.text(x, y, label, fontsize=9)

        self.canvas.draw()

def main():
    root = tk.Tk()
    app = Test(root)
    root.mainloop()

if __name__ == "__main__":
    main()
