import pandas as pd
from tabulate import tabulate
import matplotlib.pyplot as plt


def main():
    # Create a sample DataFrame
    data = {
        'Product': ['Book', 'Book', 'TShirt', 'TShirt', 'Book', 'Lego Set'],
        'Title': ['HP & the Philosophers Stone', 'HP & the Deathly Hollows', 'Gryffindor House', 'Hufflepuff House',
                  'The Hobbit', 'Hogwarts Astronomy Tower'],
        'Price': [9.99, 15.99, 25.50, 49.99, 25.99, 59.99],
        'Quantity': [126, 300, 780, 660, 1100, 1100]
    }
    # Convert the data to a data frame
    df = pd.DataFrame(data)
    # Add a new column 'Total' by multiplying 'Price' and 'Quantity'
    df['Total'] = df['Price'] * df['Quantity']
    # Apply the style
    pd.options.display.float_format = '{:.2f}'.format
    # Display the updated DataFrame
    print(tabulate(df, headers='keys', tablefmt='psql', showindex=False, stralign="left", numalign="Right"))
    # Group the data by 'Product' and sum the quantity sold and the total sales
    prodTotals = df.groupby('Product').agg({'Quantity':'sum', 'Total':'sum'}).reset_index()
    print(tabulate(prodTotals, headers='keys', tablefmt='psql', stralign="left", numalign="Right"))
    # Plot the results
    plt.figure(figsize=(8, 6))
    plt.bar(prodTotals['Product'], prodTotals['Quantity'], label='Quantity Sold', color='blue',
            bottom=prodTotals['Total'])
    plt.bar(prodTotals['Product'], prodTotals['Total'], label='Total Sales', color='red')
    # Add labels and legend
    plt.xlabel('Product')
    plt.ylabel('Amount')
    plt.title('Quantity and Total Sales by Product')
    plt.legend()
    # Display the plot
    plt.show()

    # Plot using a pie chart
    # Group the data by 'Category and calculate the sum of 'Expenses' within each group
    grouped = df.groupby('Product')['Quantity'].sum().reset_index()
    # Create a pie chart for expenses
    plt.figure(figsize=(8, 6))
    plt.pie(grouped['Quantity'], labels=grouped['Product'], autopct='%1.1f%%', startangle=140)
    plt.title('Product Distribution by Category')
    # Display the pie chart
    plt.show()

if __name__ == '__main__':
    main()
