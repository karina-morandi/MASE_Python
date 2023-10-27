from DatabaseObj_GoSales import DBConnection

def main():
    # Set the parameters that will be used to connect to the database
    print('Sample Assessment GoSales')

    host = "relational.fit.cvut.cz"
    user = "guest"
    password = "relational"
    port = 3306
    database = "GOSales"
    # Create a tuple that will store all this information
    db_Info = (host, user, password, port, database)

    # Passed the tuple to the DBConnection class
    relationalDB = DBConnection(db_Info)
    #Using the new instance of the DBConnection call the function analyseTop10QuantitySales()
    relationalDB.analyseTop10QuantitySales()
    # Next Call the function analyseProductByID(5110)
    relationalDB.analyseProductByID(5110)
    relationalDB.disposeConnection()
    # Last, close the connection and print to the console that the connection is closed


if __name__ == '__main__':
    main()


