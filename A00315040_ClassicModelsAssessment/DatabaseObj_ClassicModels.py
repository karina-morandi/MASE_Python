import pandas as pd
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
        #Unpack the connectInfo
        self.host, self.user, self.password, self.port, self.database = connectInfo
        # Create empty dataframes for each table and the merged dataframe
        self.products = None
        self.orders = None
        self.orderdetails = None
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
        # Print to the console what tables are being used
        print("\n\nUsing Table\norderdetails\norders\nproducts")
        # Call the preformEDA functions for each table
        self.preformEDA("orderdetails")
        self.preformEDA("orders")
        self.preformEDA("products")

    def preformEDA(self, tablenme):
        print("The performEDA function")
        # Print the connection progress
        #print(self.connectionProgress)
        # Print to the console what tables are being used
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
        # Call the preformEDA functions for each table
        if tablenme == "orderdetails":
            self.orderdetails = frame.copy()
        elif tablenme == "products":
            self.products = frame.copy()
        else:
            self.orders = frame.copy()

    def MergeDataFrame(self):
        print("\n\nMerged Dataframe function")
        # Refer to assessment booklet
        theDates=self.orders[['orderNumber', 'orderDate', 'requiredDate', 'shippedDate']].copy()

        theOrders=pd.merge(theDates, self.orderdetails[['orderNumber', 'productCode', 'quantityOrdered', 'priceEach']], on='orderNumber', how='inner')
        self.merged_df=pd.merge(theOrders, self.products[['productCode', 'productName', 'productLine', 'quantityInStock', 'buyPrice', 'MSRP']], on='productCode', how='inner')

        self.merged_df['discountPerUnit']=round(self.merged_df['MSRP']-(self.merged_df['priceEach']),2)

        self.merged_df['orderTotal']=round(self.merged_df['quantityOrdered']*self.merged_df['priceEach'],2)

        self.merged_df['customerSavings']=round(self.merged_df['MSRP']*(self.merged_df['quantityOrdered']-(self.merged_df['orderTotal'])),2)

        self.merged_df['profit']=round(self.merged_df['orderTotal']-(self.merged_df['buyPrice']*self.merged_df['quantityOrdered']),2)

        print(tabulate(self.merged_df.head(), headers='keys', tablefmt='pretty', showindex=True))
    def analyseTop10QuantitySales(self):
        print("The analyseTop10QuantitySales function")
        # Refer to assessment booklet
        product_sums = self.merged_df.groupby('productName').agg(
            {'productLine': 'first', 'productCode': 'count', 'quantityOrdered': 'sum', 'orderTotal': 'sum',
             'profit': 'sum'}).reset_index()
        print(tabulate(product_sums.head(), headers='keys', tablefmt='pretty', showindex=True))

        resultset = product_sums.nlargest(n=10, columns='orderTotal').sort_values('orderTotal', ascending=False)
        print(tabulate(resultset,
                       headers=['Name', 'Line', 'Number of Orders', 'Total Ordered', 'Total Sales', 'Total Profit'],
                       floatfmt='.2f', showindex=True))

        wrapped_labels = [textwrap.fill(label, 10) for label in resultset['productName']]
        print(wrapped_labels)
        # Create the main window
        root = tk.Tk()
        root.title("Top 10 Products based on Sales and Profit")
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
        ax.bar(resultset['productName'], resultset['orderTotal'], label='Total Sales', color='red')
        ax.bar(resultset['productName'], resultset['profit'], label='Total Profit', color='blue',
               bottom=resultset['orderTotal'])
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
        print("The analyseProductByID function")
        # Refer to assessment booklet
        result = self.merged_df[self.merged_df['productCode'] == prod_ID]
        # Extrapulate the order information into a new dataframe
        orders = result[['orderDate', 'requiredDate', 'shippedDate', 'quantityOrdered', 'priceEach', 'discountPerUnit', 'orderTotal', 'customerSavings', 'profit']]
       # Calculate and print the totals
        print(tabulate(orders.head(15), headers='keys', tablefmt='pretty', showindex=True))
        print('\n\n\nProduct Info based on ID: {0}\t{1}'.format(prod_ID, result['productName'].iat[0]))
        # Print the resulting dataframe
        productName = result['productName'].iat[0]
        unitPrice = result['priceEach'].iat[0]
        unitCost = result['buyPrice'].iat[0]
        total_sold = orders['quantityOrdered'].sum()
        total_sales = orders['orderTotal'].sum()
        total_profit = orders['profit'].sum()
        totalNoOrders = len(orders)
        print('Unit Price: {0}'.format(unitPrice))
        print('Unit Cost: {0}'.format(unitCost))
        print('Totals: \nOrders: {0}'.format(totalNoOrders))
        print('Sold: €{0}'.format(round(total_sold, 2)))
        print('Sales: €{0}'.format(round(total_sales, 2)))
        print('Profit: €{0}'.format(round(total_profit, 2)))
        print(tabulate(orders.head(15), headers='keys', tablefmt='pretty', showindex=True))

        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6), dpi=100)

        # Bar chart for total sales and total profit
        ax1.bar(['Total Sales', 'Total Profit'], [total_sales, total_profit], color=['blue', 'green'])
        ax1.set_ylabel('Amount in €')
        ax1.set_title('Total Sales and Total Profit')

        # Line chart for total orders per month
        orders['orderDate'] = pd.to_datetime(orders['orderDate'])  # Convert orderDate to datetime
        orders['Month'] = orders['orderDate'].dt.strftime('%Y-%m')  # Extract year and month

        monthly_orders = orders.groupby('Month').size().reset_index(name='Total Orders')

        ax2.plot(monthly_orders['Month'], monthly_orders['Total Orders'], marker='o', color='purple')
        ax2.set_xlabel('Month')
        ax2.set_ylabel('Total Orders')
        ax2.set_title('Total Orders per Month')

        # Display the charts
        plt.tight_layout()
        plt.show()


    def productLineSummary(self):
        print('Product Line Summary')
        # Refer to assessment booklet

    def printDF(self, dataF):
        print('Print the dataF using tabulate')
        print(tabulate(dataF.head(), headers='keys', tablefmt='pretty', showindex=True))
        print(tabulate(dataF.tail(), headers='keys', tablefmt='pretty', showindex=True))
        print('\n')

    def disposeConnection(self):
        print("Close the connection")
        # Close the database connection


