from DatabaseObj_ClassicModels import DBConnection

def main():
    print('Sample Assessment Classic Models')
    # Set the parameters that will be used to connect to the database
    host = "relational.fit.cvut.cz"
    user = "guest"
    password = "relational"
    port = 3306
    database = "classicmodels"
    # Create a tuple that will store all this information
    db_Info = (host, user, password, port, database)
    # Passed the tuple to the DBConnection class
    relationalDB = DBConnection(db_Info);
    #Using the new instance of the DBConnection call the function analyseTop10QuantitySales()
    relationalDB.analyseTop10QuantitySales()
    # Next call the function analyseProductByID('S72_1253')
    relationalDB. analyseProductByID('S72_1253')
    #Next call the function productLineSummary()
    relationalDB.productLineSummary()
    # Last, close the connection and print to the console that the connection is closed
    relationalDB.disposeConnection()
    print("Connection closed")

if __name__ == '__main__':
    main()