#Daniel Preller, 17 June 2025, Assignment 4.2
#Modified program to show either high or low temperatures from a data setz

import csv
from datetime import datetime
from matplotlib import pyplot as plt

#CHANGE: Original program logic moved to a function with parameters
#CHANGE: high and highs variables renamed to extreme and extremes to make sense
#Displays a chart of either the high or low temperatures
def create_fig(extreme_type, extreme_color, row_number):
    filename = 'sitka_weather_2018_simple.csv'
    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)
        dates, extremes = [], []
        for row in reader:
            current_date = datetime.strptime(row[2], '%Y-%m-%d')
            dates.append(current_date)
            extreme = int(row[row_number])#CHANGE: row number is now specified in function call
            extremes.append(extreme)

        # Plot the high temperatures.
        #plt.style.use('seaborn')
        fig, ax = plt.subplots()
        ax.plot(dates, extremes, c=extreme_color)#CHANGE: color is now variable

        # Format plot.
        plt.title(f"Daily {extreme_type} temperatures - 2018", fontsize=24)#CHANGE: extreme_type variable used to display appropriate title
        plt.xlabel('', fontsize=16)
        fig.autofmt_xdate()
        plt.ylabel("Temperature (F)", fontsize=16)
        plt.tick_params(axis='both', which='major', labelsize=16)

        plt.show()

#ADDITION: Added main function to allow users to select multiple options
def main():
    print("To see the high temperatures, enter HIGHS")
    print("To see the low temperatures, enter LOWS")
    print("To exit, enter EXIT")
    print("To select another option, close the current chart first")
    #Prints instructions

    # Displays the appropriate chart for the user's selection
    while True:
        try:
            selection = input("Please select an option: ")
            if selection.upper() not in ("HIGHS", "LOWS", "EXIT"):
                raise Exception
        except Exception:
            print(f"'{selection}' is not a valid option")
        if selection.upper() == "HIGHS":
            create_fig("high", "red", 5)
        if selection.upper() == "LOWS":
            create_fig("low", "blue", 6)
        if selection.upper() == "EXIT":
            break

    print("Thank you for viewing the data")
    print("The program will now close")
    #Exit message

if __name__ == '__main__':
    main()