import sys
import pandas as pd
from matplotlib.backends._backend_tk import FigureCanvasTk
from tabulate import tabulate
from sqlalchemy import create_engine, inspect
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import textwrap

class DBConnection:
    def __init__(self, connectInfo):
        print("Inside the Constructor")
        # Unpack the connectInfo
        self.host, self.user, self.password, self.port, self.database = connectInfo
        # Create empty dataframes for each table and the merged dataframe
        self.connectionProgress = None
        self.tableInfo = None
        self.mydb = None
        self.go_daily_sales = None
        self.go_products = None
        self.merged_df = None
        # Configure db
        self.db_config = {
            'host': self.host,
            'user': self.user,
            'password': self.password,
            'port': self.port,
            'database': self.database
        }

        # Once configured then call the ConnectNow, getConnectionProgress and MergeDataFrame functions
        self.ConnectNow()
        self.getConnectionProgress()
        self.MergeDataFrame()

    def ConnectNow(self):
        print("The ConnectNow function")
        # Print the connection data to the user so they can see what was entered
        self.connectionProgress = "New connection Using:" \
                                  "\nHost: {0}" \
                                  "\nUser: {1}" \
                                  "\nPassword: {2}" \
                                  "\nPort: {3}" \
                                  "\nDatabase: {4}\n\n".format(self.host, self.user, self.password, self.port,
                                                               self.database)

        # Establish a connection
        try:
            # Create a SQLAlchemy engine to connect to the database
            self.mydb = create_engine(
                f"mysql+mysqlconnector://{self.db_config['user']}:{self.db_config['password']}@{self.db_config['host']}:{self.db_config['port']}/{self.db_config['database']}")
            # Create an Inspector object to inspect the database
            inspector = inspect(self.mydb)
            # Get the list of table names in the database
            table_names = inspector.get_table_names()
            # Print the list of table names
            self.connectionProgress += "Tables in the database:"
            for table_name in table_names:
                self.connectionProgress += "\n" + table_name

        except Exception as error:
            # Handle the exception if the connection fails or any other error occurs
            print("Error: Unable to connect to the MySQL database")
            print(f"Error Details: {error}")

    def getConnectionProgress(self):
        print("The getConnectionProgress function")
        # Print the connection progress
        print(self.connectionProgress)
        print("\n\nUsing Table\ngo_daily_sales\ngo_products")
        self.preformEDA("go_daily_sales")
        self.preformEDA("go_products")

    def preformEDA(self, tablenme):
        print("The performEDA function")
        query = "SELECT * FROM " + tablenme
        frame = pd.read_sql(query, self.mydb);
        print("\n\n\n******************** {0} ********************".format(tablenme))
        print('\n\nPrint DataFrame Info for table {0}'.format(tablenme))
        print(frame.info())
        print('\n\nPrint Number of Unique Items in {0}'.format(tablenme))
        print(frame.nunique())
        print('\n\nPrint Number of Unique Items in Each Column for table {0}'.format(tablenme))
        print(frame.apply(pd.unique))
        print("\n\nTable: {0}".format(tablenme))
        print(tabulate(frame.head(), headers='keys', tablefmt='pretty', showindex=True))
        print(tabulate(frame.tail(), headers='keys', tablefmt='pretty', showindex=True))

        if tablenme == "go_daily_sales":
            self.go_daily_sales = frame.copy()
        else:
            self.go_products = frame.copy()

    def MergeDataFrame(self):
        print("\n\nMerged Dataframe")
        # Create a dataframe called products with just the product number, product and unit cost from the go_products table
        products = self.go_products[['Product number', 'Product', 'Unit cost']]
        # Merge this with the other frames as per the screenshot from the assessment sheet
        self.merged_df = pd.merge(products, self.go_daily_sales[['Product number', 'Date', 'Quantity', 'Unit price', 'Unit sale price']], on = 'Product number', how = 'inner')
        # Create the necessary calculated columns
        # The total sales is the quantity by the unit sale price
        # The total profit is total sales less  the unit cost  by the quantity
        self.merged_df['Total Sales'] = round(self.merged_df['Quantity']*self.merged_df['Unit sale price'],2)
        self.merged_df['Total Profit'] = round(self.merged_df['Total Sales'] - (self.merged_df['Unit cost'] * self.merged_df['Quantity']),2)
        # Print this merged dataframe to the console using printDF function
        print(tabulate(self.merged_df.head(), headers='keys', tablefmt='pretty', showindex=True))
        print(tabulate(self.merged_df.tail(), headers='keys', tablefmt='pretty', showindex=True))

    def analyseTop10QuantitySales(self):
        print("\n\nThe analyseTop10QuantitySales function")
        # Create a dataframe called product_sums that is an agg of merged_df based on the
        # screenshot in the assessment sheet
        product_sums = self.merged_df.groupby('Product').agg({'Product number':'count', 'Unit price':'first', 'Quantity':'sum', 'Total Sales':'sum', 'Total Profit': 'sum'}).reset_index()
        print(tabulate(product_sums.head(), headers='keys', tablefmt='pretty', showindex=True))
        # Creae a resultset dataframe whic is the result of the 10 nlaregest where the columns are total sales
        # Order decending
        # Print this result using tabulate and rename the headers as per the screenshot
        resultset = product_sums.nlargest(n=10, columns='Total Sales').sort_values('Total Sales', ascending=False)
        print(tabulate(resultset, headers=['Product', 'No of Sales', 'Unit Price', 'Quantity Sold', 'Total Sales', 'Total Profit'], floatfmt = '.2f', showindex=True))
        # Next create the plot but first
        # Wrapping the text for the x-labels
        wrapped_labels = [textwrap.fill(label, 10) for label in resultset['Product']]
        print(wrapped_labels)
        # Create the main window
        root = tk.Tk()
        root.title("GoSales")
        # Create a custom frame to hold the Matplotlib plot
        frame = ttk.Frame(root)
        frame.pack(expand=True, fill=tk.BOTH)
        # Create a Matplotlib figure and subplot
        # Modify the x and y labels on the axis to ensure nonscientific notation
        # and that the text is wrapped where it is too long
        fig, ax = plt.subplots(figsize=(12, 8), dpi=100)
        ax.ticklabel_format(axis='y', style='plain')
        ax.set_xticks(range(len(wrapped_labels)))
        ax.set_xticklabels(wrapped_labels)
        # Plot the two bar charts for the total sales and total product
        # Set the colour for each
        # Set the bottom chart to be the Total Sales as it is a higher value
        ax.bar(resultset['Product'], resultset['Total Sales'], label='Total Sales', color='red')
        ax.bar(resultset['Product'], resultset['Total Profit'], label='Total Profit', color='blue', bottom=resultset['Total Sales'])
        # Add the product label to the x-axis
        ax.set_xlabel('Product')
        # Add the Amount in € label to the y-axis
        ax.set_ylabel('Amount in €')
        # Set the title of the chart to be Top 10 Products based on Sales and Profit
        ax.set_title('Top 10 Products based on Sales and Profit')
        # Insert the legend
        ax.legend()
        # Create a Matplotlib canvas within the frame
        canvas = FigureCanvasTkAgg(fig, master=frame)
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        from matplotlib.backends.backend_tkagg import NavigationToolbar2Tk
        toolbar = NavigationToolbar2Tk(canvas, frame)
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        # Add a toolbar (optional)
        toolbar.update()
        # Start the Tkinter main loop
        root.mainloop()

    def analyseProductByID(self, prod_ID):
        print("\n\n\nThe analyseProductByID function")
        #Create a resultset form the merged_df based on the prodID
        result = self.merged_df[self.merged_df['Product number']==prod_ID]
        # Extrapulate the order information into a new dataframe
        orders = result[['Date', 'Quantity', 'Unit sale price', 'Total Sales', 'Total Profit']]
        # Remove any 0's
        filtered = orders[orders['Unit sale price']!=0]
        # Calculate and print the totals
        print(tabulate(orders.head(15), headers='keys', tablefmt='pretty', showindex=True))
        print('\n\n\nProduct Info based on ID: {0}\t{1}'.format(prod_ID, result['Product'].iat[0]))
        # Print the resulting dataframe
        productName = result['Product'].iat[0]
        unitPrice = result['Unit price'].iat[0]
        unitCost = result['Unit cost'].iat[0]
        total_sold = filtered['Quantity'].sum()
        total_sales = filtered['Total Sales'].sum()
        total_profit = filtered['Total Profit'].sum()
        totalNoOrders = len(filtered)
        print('Unit Price: {0}'.format(unitPrice))
        print('Unit Cost: {0}'.format(unitCost))
        print('Totals: \nOrders: {0}'.format(totalNoOrders))
        print('Sold: €{0}'.format(round(total_sold, 2)))
        print('Sales: €{0}'.format(round(total_sales, 2)))
        print('Profit: €{0}'.format(round(total_profit,2)))
        print(tabulate(filtered.head(15), headers='keys', tablefmt='pretty', showindex=True))
        # Next plot the barchart as per the screenshot in the assessment sheet
        # Create the main window
        root = tk.Tk()
        root.title("GoSales")
        # Create a custom frame to hold the Matplotlib plot
        frame = ttk.Frame(root)
        frame.pack(expand=True, fill=tk.BOTH)
        # Create a Matplotlib figure and subplot
        fig, ax = plt.subplots(figsize=(12, 8), dpi=100)
        # Modify the x and y labels on the axis to ensure nonscientific notation
        # and that the text is wrapped where it is too long
        ax.ticklabel_format(axis='y', style='plain')
        #ax.set_xticks(range(len(wrapped_labels)))
        #ax.set_xticklabels(wrapped_labels)
        # Plot the two bar charts for the total sales and total profit
        # Set the colour for each
        ax.bar('Total Sales', total_sales, label='Total Sales', color='red')
        ax.bar('Total Profit', total_profit, label='Total Profit', color='blue')
        # Add the labels to the x-axis
        ax.set_xlabel('Product')
        # Add the Amount in € label to the y-axis
        ax.set_ylabel('Amount in €')
        # Set the title of the chart
        ax.set_title('Product: {0} ({1})'.format(productName, prod_ID))
        # Insert the legend
        ax.legend()
        # Create a Matplotlib canvas within the frame
        canvas = FigureCanvasTkAgg(fig, master=frame)
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        from matplotlib.backends.backend_tkagg import NavigationToolbar2Tk
        # Add a toolbar (optional)
        toolbar = NavigationToolbar2Tk(canvas, frame)
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        toolbar.update()
        # Start the Tkinter main loop
        root.mainloop()

    def printDF(self, dataF):
        print('Print the dataF using tabulate')
        #Using tabulate print the head and tail of the dataF
        print(tabulate(dataF.head(), headers='keys', tablefmt='pretty', showindex=True))
        print(tabulate(dataF.tail(), headers='keys', tablefmt='pretty', showindex=True))
        print('\n')

    def disposeConnection(self):
        print("Close the connection")
        # Close the database connection
        self.mydb.dispose()

