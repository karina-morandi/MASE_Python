from tabulate import tabulate
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def main():
    print("Linear Regression Demo")
    housingFile_URL = 'https://davmase.z6.web.core.windows.net/csv/housingData.csv'

    housing = pd.read_csv(housingFile_URL)
    print(housing.info())
    print("\n******* Housing Data *******")
    print(tabulate(housing.head(15), headers='keys', tablefmt='pretty', showindex=True))

    housing = housing.query('sqft_living < 8000 and price < 1000000 and price > 0')
    sns.relplot(data=housing, x='sqft_above', y='price')
    plt.gcf().suptitle('Living Area & price')
    plt.show()

    # Example of little or no correlation between year built v's price
    sns.relplot(data=housing, x='yr_built', y='price')
    plt.gcf().suptitle('Year Built V Price')
    plt.show()

    # Demonstration for a pair plot
    sns.pairplot(data=housing,
                 y_vars=['price', 'sqft_living', 'sqft_above'],
                 x_vars=['price', 'sqft_living', 'sqft_above'],
                 diag_kind='kde')
    plt.gcf().suptitle('Pairplot Demo Title')
    plt.show()

    # Generate and display a correlation matrix for r values
    housing = housing.drop(columns=['date', 'street', 'city', 'statezip', 'country', 'yr_renovated', 'sqft_basement'])
    correlationMatrix =  housing.corr()
    print(tabulate(correlationMatrix.round(3), headers='keys', tablefmt='pretty', showindex=True))

    # Generate and display a heatmap
    sns.heatmap(data=housing.corr(), cmap='Blues',vmin=-1.0, vmax=1.0)
    plt.gcf().suptitle('Housing Heatmap Correlation')
    plt.show()

    # Filter the results for price only
    housingPriceCorr = round(housing.corr()[['price']].sort_values(by='price', ascending=False), 3)
    print(tabulate(housingPriceCorr, headers='keys', tablefmt='pretty', showindex=True))

    # Condense the heatmap for price only
    sns.heatmap(data=housing.corr()[['price']].sort_values(by='price', ascending=False),
                annot=True, cmap='Blues',
                cbar=False, fmt=f'.2f')
    plt.gcf().suptitle('Housing Heatmap Correlation [Price]')
    plt.show()


if __name__ == '__main__':
    main()