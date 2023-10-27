import pandas as pd
from tabulate import tabulate

def calculatePCT_Change(fires):
    print('\n******* Filtering fire data based on state,\nyear and acres burned *******')
    filterFires = fires[['state', 'fire_year', 'acres_burned']].groupby(['state', 'fire_year']).sum()
    print(filterFires)
    print('\n******* Calculating % Change *******')
    fires_pre_change = filterFires.pct_change()
    print(fires_pre_change)

def calculateRank(fires):
    print('\n******* Generating Ranked Data ******* ')
    print('Calculating Totals: ')
    rankedData = fires.groupby('state').sum()[['acres_burned', 'fire_year', 'days_burning']]
    print(rankedData.head(3))
    print('\nAdd an acres_rank column based on acres burned')
    rankedData['acres_rank'] = rankedData['acres_burned'].rank(ascending=False)
    print(rankedData.head(3))
    print('\nAdd a days_rank column based on days burning')
    rankedData['days_rank'] = rankedData.days_burning.rank(method='max')
    rankedData.sort_values('days_burning')
    print(rankedData.head(3))



def main():
    print("% Change Demo1")
    firesFile_URL = 'https://davmase.z6.web.core.windows.net/csv/fires_by_month.csv'

    fires  = pd.read_csv(firesFile_URL, index_col=[0])
    print(fires.info())
    print("\n******* Fire Data *******")
    print(tabulate(fires.head(15), headers='keys', tablefmt='pretty', showindex=True))

    #calculatePCT_Change(fires)
    calculateRank(fires)




if __name__ == '__main__':
    main()



