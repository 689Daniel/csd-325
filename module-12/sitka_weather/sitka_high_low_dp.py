#Daniel Preller, 7 August 2025, Assignment 12.2
#Redo of Assignment 4.2
#Program to show either high or low temperatures from a data set

import csv
from datetime import datetime
from matplotlib import pyplot as plt

#CHANGE: Original program moved to a function that takes an extreme type (high or low) and shows the data corresponding to that extreme type
#highs and high variables renamed to extremes and extreme to make more sense
def create_figure(extreme_type):
    filename = 'sitka_weather_2018_simple.csv'

    #Sets color and data source based on extreme type
    extreme_row = 5
    color = "red"
    if extreme_type == "high":
        extreme_row = 5
        color = "red"
    elif extreme_type == "low":
        extreme_row = 6
        color = "blue"

    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)

        # Get dates and extreme temperatures from this file.
        dates, extremes = [], []
        for row in reader:
            current_date = datetime.strptime(row[2], '%Y-%m-%d')
            dates.append(current_date)
            extreme = int(row[extreme_row])
            extremes.append(extreme)

    # Plot the extreme temperatures.
    fig, ax = plt.subplots()
    ax.plot(dates, extremes, c=color)

    # Format plot.
    plt.title(f"Daily {extreme_type} temperatures - 2018", fontsize=24)
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel("Temperature (F)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)

    plt.show()

#Addition: added main function to show instructions and allow users to select multiple options
def main():
    #Prints instructions
    print("To see high temperatures, enter HIGHS")
    print("To see low temperatures, enter LOWS")
    print("To exit, enter EXIT")
    print("To select another option, first close the current chart")

    #Selection loop for displaying the appropriate figure or exiting
    while True:
        try:
            selection = input("\nPlease select an option: ").upper()
            if selection not in ("HIGHS", "LOWS", "EXIT"):
                raise Exception
        except Exception:
            print(f"'{selection}' is not a valid option")
        if selection == "HIGHS":
            create_figure("high")
        elif selection == "LOWS":
            create_figure("low")
        elif selection == "EXIT":
            print("Thank you for viewing the data")
            print("The program will now close")
            break

if __name__ == '__main__':
    main()