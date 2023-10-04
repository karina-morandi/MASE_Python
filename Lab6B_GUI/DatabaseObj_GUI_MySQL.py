import pandas as pd
from tabulate import tabulate
import mysql.connector
import sys
# The next imports are to be used to plot
import tkinter as tk
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class DBConnection_MySQL:
    def __init__(self, connectInfo):
        self.host, self.user, self.password, self.port, self.database = connectInfo
        self.connectionProgress = None
        self.tableInfo = None
        self.cursor = None
        self.table = ""
        self.mydb = None
        self.db_config = {
            'host': self.host,
            'user': self.user,
            'password': self.password,
            'port': self.port,
            'database': self.database
        }
        self.ConnectNow()

    def ConnectNow(self):
        # Print the connection data to the user, so they can see what was entered
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
            self.mydb = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                port=self.port,
                database=self.database
            )
            self.cursor = self.mydb.cursor()
            self.cursor.execute("SHOW TABLES")
            database = [item[0] for item in self.cursor.fetchall()]
            self.connectionProgress += "Tables in the database:"
            for table_name in database:
                print(table_name)
                self.connectionProgress += "\n" + table_name

        except Exception as error:
            # Handle the exception if the connection fails or any other error occurs
            print("Error: Unable to connect to the MySQL database")
            print(f"Error Details: {error}")

    def getConnectionProgress(self):
        return self.connectionProgress

    def preformEDA(self):
        query = "SELECT * FROM " + self.table
        frame = pd.read_sql(query, self.mydb);
        pd.set_option('display.expand_frame_repr', False)
        # print(frame)
        # Redirect stdout to a file
        with open('tableInfo.txt', 'w') as f:
            sys.stdout = f
            print('\n\nPrint DataFrame Info for table {0}'.format(self.table))
            print(frame.info())
            print('\n\nPrint Number of Unique Items in {0}'.format(self.table))
            print(frame.nunique())
            print('\n\nPrint Number of Unique Items in Each Column for table {0}'.format(self.table))
            print(frame.apply(pd.unique))
            print("\n\nTable: {0}".format(self.table))
            print(tabulate(frame.head(), headers='keys', tablefmt='pretty', showindex=True))
            print(tabulate(frame.tail(), headers='keys', tablefmt='pretty', showindex=True))

        # Reset stdout to the original value
        sys.stdout = sys.__stdout__

    def visualiseClient(self):
        query = "SELECT * FROM client"
        frame = pd.read_sql(query, self.mydb)
        values = frame['gender'].value_counts(dropna=False)
        labels = frame['gender'].unique().tolist()

        # Create the main window
        root = tk.Tk()
        root.title("Gender")

        # Create a custom frame to hold the Matplotlib plot
        frame = ttk.Frame(root)
        frame.pack(expand=True, fill=tk.BOTH)

        # Create a Matplotlib figure and subplot
        fig = Figure(figsize=(5, 4), dpi=100)
        subplot = fig.add_subplot(111)
        subplot.pie(values, labels=labels, autopct='%1.1f%%', startangle=90)  # Example data

        # Create a Matplotlib canvas within the frame
        canvas = FigureCanvasTkAgg(fig, master=frame)
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

        # Add a toolbar(optional)
        from matplotlib.backends.backend_tkagg import NavigationToolbar2Tk
        toolbar = NavigationToolbar2Tk(canvas, frame)
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        toolbar.update()

        # Start the Tkinter main loop
        root.mainloop()

    def selectTable(self, tablename):
        print("Establishing a connect to table: {0}".format(tablename))
        self.table = tablename
        self.preformEDA()

    def printDF(self, dataF):
        print(tabulate(dataF.head(), headers='keys', tablefmt='pretty', showindex=True))
        print(tabulate(dataF.tail(), headers='keys', tablefmt='pretty', showindex=True))
        print('\n')

    def disposeConnection(self):
        # Close database connection
        self.cursor.close()
