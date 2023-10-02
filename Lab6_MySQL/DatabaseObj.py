import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import create_engine, inspect
from tabulate import tabulate


class DBConnection:
    def __init__(self, connectInfo):
        self.host, self.user, self.password, self.port, self.database = connectInfo
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
        # Print the connection data to the user so they can see what was entered
        print("New connection Using:"
              "\nHost: {0}"
              "\nUser: {1}"
              "\nPassword: {2}"
              "\nPort: {3}"
              "\nDatabase: {4}\n\n".format(self.host, self.user, self.password, self.port, self.database))
        # Establish a connection
        try:
            # Create a SQLAlchemy engine to connect to the database
            self.mydb = create_engine(
                f"mysql+mysqlconnector://{self.db_config['user']}:{self.db_config['password']}@{self.db_config['host']}:{self.db_config['port']}/{self.db_config['database']}")
                #f"mysql+mysqlconnector://{self.db_config['user']}:{self.db_config['password']}@{self.db_config['host']}:{self.db_config['port']}/{self.db_config['database']}")
            # Create an Inspector object to inspect the database
            inspector = inspect(self.mydb)
            # Get the list of table names in the database
            table_names = inspector.get_table_names()
            # Print the list of table names
            print("Tables in the database:")
            for table_name in table_names:
                print(table_name)

        except Exception as error:
            # Handle the exception if the connection fails or any other error occurs
            print("Error: Unable to connect to the MySQL database")
            print(f"Error Details: {error}")

    def preformEDA(self):
        frame = pd.read_sql(f"SELECT * FROM {self.table}", self.mydb);
        pd.set_option('display.expand_frame_repr', False)
        print('\n\nPrint DataFrame Info for table {0}'.format(self.table))
        print(frame.info())
        print('\n\nPrint Number of Unique Items in {0}'.format(self.table))
        print(frame.nunique())
        print("\n\nPrint Number of Unique Items in Each Column for table {0}".format(self.table))
        print(frame.apply(pd.unique))
        print("\n\nTable")
        self.printDF(frame)

    def visualiseClient(self):
        frame = pd.read_sql(f"SELECT * FROM client", self.mydb);
        pd.set_option('display.expand_frame_repr', False)
        values = frame['gender'].value_counts(dropna=False)
        labels = frame['gender'].unique().tolist()
        plt.pie(values, labels=labels, autopct='%.1f%%')
        plt.legend(labels)
        plt.savefig("Gener.png")
        plt.show()

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
        self.mydb.dispose()
