import pandas as pd
from tabulate import tabulate


def main():
    print("Agg Demo1")
    firesFile_URL = 'https://davmase.z6.web.core.windows.net/csv/fires_by_month.csv'

    fires  = pd.read_csv(firesFile_URL, index_col=[0])
    print(fires.info())
    print("\n******* Fire Data *******")
    print(tabulate(fires.head(15), headers='keys', tablefmt='pretty', showindex=True))

    print("\n******* Mean Fire Data *******")
    meanFires = fires.groupby('state').mean().round(2)
    print(tabulate(meanFires.head(15), headers='keys', tablefmt='pretty', showindex=True))

    print("\n******* Fire Data Year/Month *******")
    meanFires2 = fires.groupby(['state', 'fire_year', 'fire_month']).mean().round(2)
    print(meanFires2)

    print("\n******* Data grouped by Year totals *******")
    yearly_group = fires.groupby('fire_year')
    yearly_sums = yearly_group.sum()
    yearly_sums = yearly_sums.drop(['state', 'fire_month'], axis=1) #The one is for the columns
    print(yearly_sums.head(3))

    print("\n******* Burning days by State Year Month totals *******")
    monthly_group_BD = fires.groupby(['state', 'fire_year', 'fire_month']).agg({'days_burning': ['sum', 'count', 'mean']})
    #print(tabulate(monthly_group_BD.head(3), headers='keys', tablefmt='pretty', showindex=True))
    print(monthly_group_BD)

    print("\n******* Data grouped by State Year Month totals *******")
    monthly_group = fires.groupby(['state', 'fire_year', 'fire_month']).agg({'acres_burned':['sum', 'count', 'mean'], 'days_burning': ['sum', 'count', 'mean']})
    print(tabulate(monthly_group.head(3), headers='keys', tablefmt='pretty', showindex=True))
    #print(monthly_group)


if __name__ == '__main__':
    main()



