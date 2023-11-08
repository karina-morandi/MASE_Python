from DatabaseObj_GoSales import DBConnection

def main():
    # Set the parameters that will be used to connect to the database
    host = "relational.fit.cvut.cz"
    user = "guest"
    password = "relational"
    port = 3306
    database = "GOSales"
    # Create a tuple that will store all this information
    db_Info = (host, user, password, port, database)
    # Passed the tuple to the DBConnection class
    relationalDB= DBConnection(db_Info);
    # This application already knows what tables to use to the following
    # line of code runs the routines to get the information from the table
    #relationalDB.analyseTop10QuantitySales()
    relationalDB.analyseProductByID(5110)
    relationalDB.disposeConnection()
    print("Connection closed")

if __name__ == '__main__':
    main()