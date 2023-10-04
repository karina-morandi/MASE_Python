import pandas as pd
from tabulate import tabulate

def printDF(dataF, printOpt):
    if printOpt == True:
        print(tabulate(dataF, headers='keys', tablefmt='pretty', showindex=True))
    else:
        print(tabulate(dataF.head(), headers='keys', tablefmt='pretty', showindex=True))
        print(print(tabulate(dataF.tail(), headers='keys', tablefmt='pretty', showindex=True)))
    print('\n')

def testDateConversion(dataF):
    """This next bit is for testing purposes:
            1. Copy the following columns into a new dataframe called date_columns
            2. Print the info on this new dataframe
            3. Print the head and tail for this dataframe
            4. Convert the these columns to a different format
            5. Print out the new formatted columns and check the difference"""
    # 1
    date_columns = dataF[['startdate', 'enddate', 'createddate', 'timestamp']].copy()
    # 2
    print(date_columns.info())
    # 3
    printDF(date_columns, False)
    # 4
    date_columns['startdate'] = pd.to_datetime(date_columns['startdate']).dt.strftime('%d-%m-%y')
    date_columns['enddate'] = pd.to_datetime(date_columns['enddate']).dt.strftime('%d-%m-%y')
    date_columns['createddate'] = pd.to_datetime(date_columns['createddate']).dt.strftime('%d-%m-%y')
    date_columns['timestamp'] = pd.to_datetime(date_columns['timestamp']).dt.strftime('%d-%m-%y %H:%M:%S')
    # 5
    printDF(date_columns, False)


def main():
    # Download the file from the server
    file_path = 'https://davmase.z6.web.core.windows.net/data/president_polls_2016.csv'
    # Load a dataframe called polls
    polls = pd.read_csv(file_path, verbose=True)
    # Print the dataframe info and then print the head and tail of the dataframe
    print('Print DataFrame Info')
    print(polls.info())
    print('\nPrint Head & Tail')
    printDF(polls, False)
    testDateConversion(polls)



if __name__ == "__main__":
    main()