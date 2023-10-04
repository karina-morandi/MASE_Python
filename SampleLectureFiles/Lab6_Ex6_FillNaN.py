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
    # Fill NaN values with mean values
    print("Calculate mean for distance column")
    meanFill = df.copy()
    meanFill['Distance'].fillna(value = df['Distance'].mean(), inplace=True)
    printDF(meanFill)

    # Use interpolate to fill NaN values in dataframe
    print("Interpolating NaN values")
    intrepo = df.copy()
    interpo = intrepo.interpolate()
    printDF(interpo)




if __name__=='__main__':
    main()


