from tabulate import tabulate
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


def main():
    print("Sklearn Predictions Demo")
    housingFile_URL = 'https://davmase.z6.web.core.windows.net/csv/housingData.csv'

    housing = pd.read_csv(housingFile_URL)
    print(housing.info())
    print("\n******* Housing Data *******")
    # Filter the data down to the previous example
    housing = housing.query('sqft_living < 8000 and price < 1000000 and price > 0')
    # Drop some of the columns
    housing = housing.drop(columns=['date', 'street', 'city', 'statezip', 'country', 'yr_renovated', 'sqft_basement'])
    print(tabulate(housing.head(15), headers='keys', tablefmt='pretty', showindex=True))

    # Plotting a simple linear regression Model
    sns.lmplot(data=housing, x='sqft_living', y='price', ci=None, scatter_kws={'s': 5}, line_kws={'color': 'red'})
    plt.gcf().suptitle('Simple Linear Regression')
    plt.show()

    # -----------Training and testing a model for predictions
    # Step 1: Split the data into the training and test datasets
    x_train, x_test, y_train, y_test = train_test_split(housing[['sqft_living']], housing[['price']],test_size=0.33, random_state=42)
    # Step 2: Create the model from the training dataset
    linearModel = LinearRegression()
    linearModel.fit(x_train, y_train)
    # Step 3: Validate the model with the test dataset
    linearModel.score(x_test, y_test)
    print('Linear Model Score: {0}'.format(linearModel.score(x_test, y_test)))
    # Step 4: Use the model to make predictions
    y_predicted = linearModel.predict(x_test)
    print(y_predicted)

    # ************************************************************************
    # Prepare the data for plotting
    # Step 1: Put the predicted values in a DataFrame
    predicted = round(pd.DataFrame(y_predicted, columns=['price_predicted']), 2)
    # Step 2: Combine the test data and the predicted data
    combined = predicted.join([x_test.reset_index(drop=True), y_test.reset_index(drop=True)])
    # Step 3: Melt the price and price_predicted columns into a single column
    melted = pd.melt(combined, id_vars=['sqft_living'],
                     value_vars=['price', 'price_predicted'],
                     var_name='price_type', value_name='price_value')
    print('Meleted Dataframe')
    print(tabulate(melted.head(), headers='keys', tablefmt='pretty', showindex=True))
    # Plot the data
    sns.relplot(data=melted, x='sqft_living', y='price_value', hue='price_type')
    plt.gcf().suptitle('Predicted Price')
    plt.show()

    # Calculate and plot the residuals
    print('Residual Dataframe')
    combined['residual'] = round(combined.price - combined.price_predicted, 2)
    print(tabulate(combined.head(), headers='keys', tablefmt='pretty', showindex=True))
    g = sns.relplot(data=combined, x='sqft_living', y='residual')
    # draw a horizontal line where the Y axis is 0
    for ax in g.axes.flat:
        ax.axhline(0, ls='--')
    plt.gcf().suptitle('Residuals')
    plt.show()


if __name__ == '__main__':
    main()