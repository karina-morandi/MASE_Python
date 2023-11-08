from CSVObj_GoSales import DBConnection

def main():
    # Set the urls that will be used to connect to the database
    go_daily_sales_URL = 'https://davmase.z6.web.core.windows.net/GoSales/go_daily_sales.csv'
    go_products_URL = 'https://davmase.z6.web.core.windows.net/GoSales/go_products.csv'
    # Create a tuple and pack the information
    csvFiles = (go_daily_sales_URL, go_products_URL)
    # Passed the tuple to the DBConnection class
    relationalDB= DBConnection(csvFiles);
    # This application already knows what tables to use to the following
    # line of code runs the routines to get the information from the table
    relationalDB.analyseTop10QuantitySales()
    relationalDB.analyseProductByID(5110)
    print("Connection closed")

if __name__ == '__main__':
    main()