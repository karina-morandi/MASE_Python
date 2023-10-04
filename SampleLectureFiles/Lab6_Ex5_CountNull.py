import numpy as np
import pandas as pd
from tabulate import tabulate

def printDF(dataF):
    print(tabulate(dataF, headers='keys', tablefmt='pretty', showindex=True))
    print('\n')

def main():
    data = {
        "Day": ['Mon', 'Tue', 'Wed', 'Thur', 'Fri', 'Sat', 'Sun'],
        "Category": ['Run', 'Run', 'Walk', 'Run', 'Rest', 'Run', 'Walk'],
        "Distance": [10, None, 5.6, 10, None, 32.2, 5],
        "Time": [53, 102, 72, 55, np.nan, 187, 58],
        "Calories": [769, 967, 387, 788, None, 2559, 340]
    }
    df = pd.DataFrame(data)
    printDF(df)
    # Count the missing values in each column
    missing_count = df.isna().sum()
    print("Count of Missing Values in Each Column:")
    print(missing_count)
    # Display all rows that contain NA values
    missing_rows = df[df.isnull().any(axis=1)]
    printDF(missing_rows)
    # Display all rows that dont have NA values
    complete_rows = df.dropna(how='any')
    printDF(complete_rows)



if __name__=='__main__':
    main()


