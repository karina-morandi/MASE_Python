import pandas as pd
from tabulate import tabulate

def main():
    print("nlargest Demo1")
    carsFile_URL = 'https://davmase.z6.web.core.windows.net/csv/cars.csv'

    cars  = pd.read_csv(carsFile_URL, index_col=[0])
    print(cars.info())
    print("\n******* Car Data *******")
    print(tabulate(cars.head(10), headers='keys', tablefmt='pretty', showindex=True))

    print('\nTop 5 Cars based on engine size')
    top10Engine = cars.nlargest(n=5, columns='enginesize')
    print(tabulate(top10Engine, headers='keys', tablefmt='pretty', showindex=True))

    print('\nTop 5 Cars based on engine size & price')
    top10EnginePrice = cars.nlargest(n=5, columns=['enginesize', 'price'])
    print(tabulate(top10EnginePrice, headers='keys', tablefmt='pretty', showindex=True))


if __name__ == '__main__':
    main()

