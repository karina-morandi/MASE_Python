import pandas as pd
from tabulate import tabulate
import matplotlib.pyplot as plt

def main():
    print("Pivot Demo1")
    firesFile_URL = 'https://davmase.z6.web.core.windows.net/csv/fires_by_month.csv'

    fires  = pd.read_csv(firesFile_URL, index_col=[0])
    print(fires.info())
    print("\n******* Fire Data *******")
    print(tabulate(fires.head(15), headers='keys', tablefmt='pretty', showindex=True))

    print("\n******* Data for states: AK, CA, ID TX *******")
    selected_values =  ['AK','CA','ID','TX']
    top_states = fires.groupby(['state', 'fire_year'], as_index=False).sum()
    top_states = top_states.query('state in @selected_values')
    print(top_states.head(2))

    print("\n******* Pivot states: AK, CA, ID TX *******")
    print(top_states.pivot(index='fire_year', columns='state', values='acres_burned').head(2))
    top_states.pivot(index='fire_year', columns='state',values='acres_burned').plot()
    plt.xlabel('Year')
    plt.ylabel('Acres burned')
    plt.title('Acres burned by year')
    plt.show()

    print("\n******* Pivot new DF - states: AK, CA, ID TX *******")
    fires_top_4 = fires.query('state in @selected_values')
    fires_top_4 = fires_top_4.pivot_table(index='fire_year', columns='state', values='acres_burned', aggfunc='sum')
    print(fires_top_4.head(2))


if __name__ == '__main__':
    main()



