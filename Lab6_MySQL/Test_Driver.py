from DatabaseObj import DBConnection


def main():
    # Set the parameters that will be used to connect to the database
    host = "relational.fit.cvut.cz"
    user = "guest"
    password = "relational"
    port = 3306
    database = "financial"
    # Create a tuple that will store all this information
    db_Info = (host, user, password, port, database)
    # Passed the tuple to the DBConnection class
    relationalDB = DBConnection(db_Info);
    # Ask the user to enter a table name
    table = input("\nEnter table name: ")
    # Print the table name back to the user
    print("Table selected: {0}".format(table))
    # Call the method selectTable and pass the table variable to it
    relationalDB.selectTable(table)
    # Call a method that will visualise the client ratio
    relationalDB.visualiseClient()
    # Close the connection
    relationalDB.disposeConnection()
    print("Connection closed")


if __name__ == '__main__':
    main();
