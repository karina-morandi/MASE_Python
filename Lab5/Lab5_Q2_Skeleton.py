import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from tabulate import tabulate


def caloriesBurned(dataF, calories):
    print("\n\nQuery Results: Activities where < {0} calories were burned".format(calories))
    condition = dataF['Calories'] < calories
    filtered_df = dataF.loc[condition]
    printDF(filtered_df)


def calorieTotals(dataF):
    # Create a new dataframe using groupby and sum
    activityCalorieSum = dataF.groupby('Category')['Calories'].sum().to_frame()
    # Print the result
    print(tabulate(activityCalorieSum, headers='keys', tablefmt='pretty', showindex=True))
    # Plot using Piechart, set the title and show plot
    activityCalorieSum.plot(kind="pie", autopct='%.2f%%', subplots=True)
    plt.title("Total Calories Burned")
    plt.show()


def distanceQuery(dataF, low, high):
    print("\n\nQuery Results: Activities beteeen {0}klm - {1}klm".format(low, high))
    query1 = dataF.query('Distance >= @low and Distance <= @high')
    query1.plot(kind="bar", x="Day", y="Distance")
    plt.title("Activities between {0}klm - {1}klm".format(low, high))
    plt.xticks(rotation=0)
    plt.show()
    printDF(query1)


def runTimeQuery(dataF, time):
    print("\n\nQuery Results: Running activities more than {0} minutes".format(time))
    query1 = dataF.query('`Category` == "Run" and Time > @time')
    printDF(query1)


def cleanRestDays(dataF):
    dataF[['Distance', 'Time', 'Calories']] = dataF[['Distance', 'Time', 'Calories']].apply(pd.to_numeric,
                                                                                            errors='coerce')
    return dataF


def calculateSpeed(dataF):
    print("Calculating Speed")
    for i, (d, t) in enumerate(zip(dataF['Distance'], dataF['Time'])):
        try:
            dataF.loc[i, 'Speed'] = round(d / (t / 60), 2)
        except ZeroDivisionError:
            dataF.loc[i, 'Speed'] = np.nan
    return dataF


def calculateRunTotals(dataF):
    runQuery = dataF.query('`Category` == "Run"')
    totalTime = runQuery['Time'].sum()
    totalRuns = len(runQuery.index)
    totalDistance = runQuery['Distance'].sum()
    totalCalories = runQuery['Calories'].sum()
    averageSpeed = runQuery['Speed'].mean()
    print("\nAnalysis for the runs during the week"
          "\nNumber of Runs:\t\t\t\t{0}"
          "\nTotal Distance:\t\t\t\t{1:.2f}klm"
          "\nTotal Calories Burned:\t{2:.2f}"
          "\nTotal Running Time:\t\t\t{3:.0f}minutes"
          "\nAverage Speed:\t\t\t\t{4:.2f}klm/hour".format(totalRuns, totalDistance, totalCalories, totalTime,
                                                           averageSpeed))


def calculateWalkTotals(dataF):
    totalTime = dataF.loc[dataF['Category'] == 'Walk', 'Time'].sum()
    totalWalks = dataF['Category'].value_counts()['Walk']
    totalDistance = dataF.loc[dataF['Category'] == 'Walk', 'Distance'].sum()
    totalCalories = dataF.loc[dataF['Category'] == 'Walk', 'Calories'].sum()
    averageSpeed = dataF.loc[dataF['Category'] == 'Walk', 'Speed'].mean()

    print("\nAnalysis for the walks during the week"
          "\nNumber of Walks:\t\t\t{0}"
          "\nTotal Distance:\t\t\t\t{1:.2f}klm"
          "\nTotal Calories Burned:\t\t{2:.2f}"
          "\nTotal Running Time:\t\t\t{3:.0f}minutes"
          "\nAverage Speed:\t\t\t\t{4:.2f}klm/hour".format(totalWalks, totalDistance, totalCalories, totalTime,
                                                           averageSpeed))


def printDF(dataF):
    print(tabulate(dataF, headers='keys', tablefmt='pretty', showindex=False))
    print('\n')


def main():
    data = {
        "Day": ['Mon', 'Tue', 'Wed', 'Thur', 'Fri', 'Sat', 'Sun'],
        "Category": ['Run', 'Run', 'Walk', 'Run', 'Rest', 'Run', 'Walk'],
        "Distance": [10, 12, 5.6, 10, "Rest", 32.2, 5],
        "Time": [53, 102, 72, 55, "Rest", 187, 58],
        "Calories": [769, 967, 387, 788, "Rest", 2559, 340]
    }

    # load data into a DataFrame object:
    df = pd.DataFrame(data)
    printDF(df)

    df = cleanRestDays(df)
    printDF(df)

    df = calculateSpeed(df)
    printDF(df)

    calorieTotals(df)

    caloriesBurned(df, 500)

    distanceQuery(df, 10, 12)

    runTimeQuery(df, 54)

    calculateRunTotals(df)

    calculateWalkTotals(df)


if __name__ == '__main__':
    print("Data Analysis & Visualisation\n")
    main()
