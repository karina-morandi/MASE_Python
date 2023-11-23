import pandas as pd
import geopandas as gpd
from shapely.geometry import Point
import matplotlib.pyplot as plt

# Sample data with coordinates
data = {
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 'Philadelphia', 'San Antonio', 'San Diego', 'Dallas', 'San Jose'],
    'Population': [8623000, 4000000, 2716000, 2326000, 1664000, 1584000, 1532000, 1497000, 1341000, 1033000],
    'Latitude': [40.7128, 34.0522, 41.8781, 29.7604, 33.4484, 39.9526, 29.4241, 32.7157, 32.7767, 37.3382],
    'Longitude': [-74.0060, -118.2437, -87.6298, -95.3698, -112.0740, -75.1652, -98.4936, -117.1611, -96.7970, -121.8863]
}

# Creating a GeoDataFrame
gdf = gpd.GeoDataFrame(data, geometry=[Point(xy) for xy in zip(data['Longitude'], data['Latitude'])])

# Filter the world GeoDataFrame to include only North America
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
north_america = world[world.continent == 'North America']

# Plotting the data for North America
fig, ax = plt.subplots(figsize=(12, 8))
north_america.boundary.plot(ax=ax, color='lightgrey', edgecolor='black', linewidth=0.8)
gdf.plot(ax=ax, color='red', marker='o', markersize=50, alpha=0.5)

for x, y, label in zip(gdf.geometry.x, gdf.geometry.y, gdf['City']):
    ax.text(x, y, label, fontsize=9)

plt.title('Population Distribution in Major US Cities')
plt.show()
