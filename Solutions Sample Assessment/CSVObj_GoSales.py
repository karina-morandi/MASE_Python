import pandas as pd
from tabulate import tabulate
from sqlalchemy import create_engine, inspect
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import textwrap

#https://relational.fit.cvut.cz/dataset/GOSales

class DBConnection:
    def __init__(self, urls):
        # Unpack the URL's
        self.go_daily_sales_URL,  self.go_products_URL = urls
        # Create empty dataframes for each table
        self.go_daily_sales = None
        self.go_products = None
        self.merged_df = None

        # Connect and merge dataframes
        self.getConnectionProgress()
        self.MergeDataFrame()

    def getConnectionProgress(self):
        print("\n\nUsing tables:\ngo_daily_sales\ngo_products")
        self.preformEDA('go_daily_sales', self.go_daily_sales_URL )
        self.preformEDA('go_products', self.go_products_URL)


    def preformEDA(self, tablenme, url):
        frame =  pd.read_csv(url)
        print('\n\n\n\n***************** {0} ***************** '.format(tablenme))
        print('\nPrint DataFrame Info for table: {0}'.format(tablenme))
        print(frame.info())
        print('\n\nPrint Number of Unique Items in {0}:'.format(tablenme))
        print(frame.nunique())
        print('\n\nPrint Number of Unique Items in Each Column for table {0}:'.format(tablenme))
        print(frame.apply(pd.unique))
        print("\n\nTable: {0}".format(tablenme))
        print(tabulate(frame.head(), headers='keys', tablefmt='pretty', showindex=True))
        print(tabulate(frame.tail(), headers='keys', tablefmt='pretty', showindex=True))

        if tablenme == 'go_daily_sales':
            self.go_daily_sales = frame.copy()
        else:
            self.go_products = frame.copy()

    def MergeDataFrame(self):
        print("\n\nMerged Dataframe")
        # Create a dataframe with just the products and product ID
        products = self.go_products[['Product number', 'Product', 'Unit cost']]
        self.merged_df = pd.merge(products, self.go_daily_sales[
            ['Product number', 'Date', 'Quantity', 'Unit price', 'Unit sale price']], on='Product number', how='inner')
        self.merged_df['Total Sales'] = round(self.merged_df['Quantity'] * self.merged_df['Unit sale price'], 2)
        self.merged_df['Total Profit'] = round(self.merged_df['Total Sales'] - (self.merged_df['Unit cost'] * self.merged_df['Quantity']), 2)
        self.printDF(self.merged_df)


    def analyseTop10QuantitySales(self):
        product_sums = self.merged_df.groupby('Product').agg({'Product number':'count', 'Unit price': 'first','Quantity':'sum', 'Total Sales':'sum', 'Total Profit':'sum'}).reset_index()
        print("Product Totals")

        resultset = product_sums.nlargest(n=10, columns=['Total Sales']).sort_values('Total Sales', ascending=False)

        print(tabulate(product_sums.nlargest(n=10, columns=['Total Sales']), headers=['Product', 'No of Sales', 'Unit Price', 'Quantity Sold', 'Total Sales', 'Total Profit'], floatfmt=".2f"))

        # Wrapping the text for the x-labels
        wrapped_labels = [textwrap.fill(label, 10) for label in resultset['Product']]

        # Create the main window
        root = tk.Tk()
        root.title("Gender")

        # Create a custom frame to hold the Matplotlib plot
        frame = ttk.Frame(root)
        frame.pack(expand=True, fill=tk.BOTH)

        # Create a Matplotlib figure and subplot
        fig, ax = plt.subplots(figsize=(12,8))

        # Modify the x and y labels on the axis to ensure nonscientific notation
        # and that the text is wrapped where it is too long
        ax.ticklabel_format(axis="y", style="plain")
        ax.set_xticks(range(len(wrapped_labels)))
        ax.set_xticklabels(wrapped_labels)

        # Plot the two bar charts for the total sales and total product
        # Set the colour for each
        # Set the bottom chart to be the Total Sales as it is a higher value
        # Add the product label to the x-axis
        # Add the Amount in € label to the y-axis
        # Set the title of the chart to be Top 10 Products based on Sales and Profit
        # Insert the legend
        ax.bar(resultset['Product'], resultset['Total Sales'], label='Total Sales', color='red')  # Example data
        ax.bar(resultset['Product'], resultset['Total Profit'], label='Total Profit', color='blue',  bottom=resultset['Total Sales'])  # Example data
        ax.set_xlabel('Product')
        ax.set_ylabel('Amount in €')
        ax.set_title('Top 10 Products based on Sales and Profit')
        ax.legend()

        # Create a Matplotlib canvas within the frame
        canvas = FigureCanvasTkAgg(fig, master=frame)
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

        # Add a toolbar (optional)
        from matplotlib.backends.backend_tkagg import NavigationToolbar2Tk
        toolbar = NavigationToolbar2Tk(canvas, frame)
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        toolbar.update()

        # Start the Tkinter main loop
        root.mainloop()

    def analyseProductByID(self, prod_ID):
        result = self.merged_df[self.merged_df['Product number'] == prod_ID]
        #result = result.groupby(['Product number', 'Product', 'Unit cost']).count()
        orders = result[['Date', 'Quantity', 'Unit sale price', 'Total Sales', 'Total Profit']]
        filtered = orders[orders['Unit sale price'] != 0]
        print("Product Info based on ID: {0}\t{1}".format(prod_ID, result['Product'].iat[0]))
        unitPrice = result['Unit price'].iat[0]
        unitCost = result['Unit cost'].iat[0]
        total_sold = filtered['Quantity'].sum()
        total_sales = filtered['Total Sales'].sum()
        total_profit = filtered['Total Profit'].sum()
        totalNoOrders = len(filtered)
        print('Unit Price:€{0}'.format(unitPrice))
        print('Unit cost: €{0}'.format(unitCost))
        print('Totals:\nOrders: {0}'.format(totalNoOrders))
        print('Sold: €{0}'.format(total_sold))
        print('Sales: €{0}'.format(round(total_sales,2)))
        print('Profit: €{0}'.format(round(total_profit,2)))
        print(tabulate(filtered, headers='keys', tablefmt='pretty', showindex=True))

        # Create the main window
        root = tk.Tk()
        root.title("Gender")

        # Create a custom frame to hold the Matplotlib plot
        frame = ttk.Frame(root)
        frame.pack(expand=True, fill=tk.BOTH)

        # Create a Matplotlib figure and subplot
        fig, ax = plt.subplots(figsize=(12, 8))

        # Modify the x and y labels on the axis to ensure nonscientific notation
        # and that the text is wrapped where it is too long
        ax.ticklabel_format(axis="y", style="plain")
        #ax.set_xticks()
        #ax.set_xticklabels(wrapped_labels)

        # Plot the two bar charts for the total sales and total product
        # Set the colour for each
        # Set the bottom chart to be the Total Sales as it is a higher value
        # Add the product label to the x-axis
        # Add the Amount in € label to the y-axis
        # Set the title of the chart to be Top 10 Products based on Sales and Profit
        # Insert the legend
        ax.bar('Total Sales', total_sales, label='Total Sales', color='red')  # Example data
        ax.bar('Total Profit', total_profit, label='Total Sales', color='blue')  # Example data
        ax.set_xlabel('Sales')
        ax.set_ylabel('Amount in €')
        ax.set_title('Product: {0} ({1})'.format(result['Product'].iat[0], prod_ID, prod_ID))
        ax.legend()

        # Create a Matplotlib canvas within the frame
        canvas = FigureCanvasTkAgg(fig, master=frame)
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

        # Add a toolbar (optional)
        from matplotlib.backends.backend_tkagg import NavigationToolbar2Tk
        toolbar = NavigationToolbar2Tk(canvas, frame)
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        toolbar.update()

        # Start the Tkinter main loop
        root.mainloop()


    def printDF(self, dataF):
        print(tabulate(dataF.head(), headers='keys', tablefmt='pretty', showindex=True))
        print(tabulate(dataF.tail(), headers='keys', tablefmt='pretty', showindex=True))
        print('\n')
