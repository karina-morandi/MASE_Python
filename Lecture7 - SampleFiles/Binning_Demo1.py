import pandas as pd
from tabulate import tabulate
import seaborn as sns
import matplotlib.pyplot as plt

theBins = [0, 100000, 200000, 300000, 400000]
theLabels = ['small', 'medium', 'large', 'very large']

def Cut_Binning(fires_filtered):
    print("\n******* Binned Fire Data: 2010 Burning days > 0 *******")
    binned_fires_filtered = pd.cut(fires_filtered['acres_burned'], bins=4)
    print(binned_fires_filtered)
    print('\nAdding labels to the bins')
    binned_fires_filtered = pd.cut(fires_filtered['acres_burned'], bins=theBins, labels=theLabels)
    print(binned_fires_filtered)
    print('\nCounting data')
    binned_fires_filtered = pd.cut(fires_filtered.acres_burned, bins=theBins, labels=theLabels).value_counts()
    print(binned_fires_filtered)

def CurC_Binning(fires_filtered):
    print('Example using 4 quantiles to bin the data')
    uniqueBins = pd.qcut(fires_filtered.acres_burned, q=4, labels=theLabels)
    print(uniqueBins)
    print('\nThe distribution of values in each bin:')
    uniqueBins = pd.qcut(fires_filtered.acres_burned, q=4, labels=theLabels).value_counts()
    print(uniqueBins)
    print('\nAssigning bin labels to a new column')
    fires_filtered['fire_size'] = pd.qcut(fires_filtered.acres_burned, q = 4, labels = theLabels)
    print(fires_filtered)

    sns.catplot(data=fires_filtered, kind='count', x='fire_month', hue='fire_size')
    plt.xlabel('Month')
    plt.ylabel('Count')
    plt.show()



def main():
    print("Binning Demo1")
    firesFile_URL = 'https://davmase.z6.web.core.windows.net/csv/fires_by_month.csv'

    fires  = pd.read_csv(firesFile_URL, index_col=[0])
    print(fires.info())
    print("\n******* Fire Data *******")
    print(tabulate(fires.head(15), headers='keys', tablefmt='pretty', showindex=True))

    print("\n******* Fire Data: 2010 Burning days > 0 *******")
    fires_filtered = fires.query('fire_year == 2010 and days_burning > 0').dropna()
    print(fires_filtered)

    #Cut_Binning(fires_filtered)
    CurC_Binning(fires_filtered)




if __name__ == '__main__':
    main()



