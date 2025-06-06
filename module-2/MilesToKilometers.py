#Daniel Preller, 1 April 2025, Assignment 4.2
#Program to convert the number of miles driven to kilometers

def main(): #Defines the main function
    while True: #Continues loop until no errors are found
        try:
            miles = float(input("Please enter the number of miles driven: ")) #Gets user input

            if miles < 0:
                raise Exception
            #Raises exception if input is negative

        except:
            print("An error has occurred. Miles driven must be a positive number.")
        #Promts user to re-enter input if miles driven is negative, or if a number is not entered

        else:
            break
        #Breaks out of the error checking loop if no errors are detected

    kilometers = convertToKilometers(miles)
    print(f"You have driven {miles:.6g} mile{checkPlural(miles)}, which is equal to {kilometers:.6g} kilometer{checkPlural(kilometers)}.")
    #Converts miles to kilometers and prints the results, formatting miles and kilometers with proper grammar if they are singular

def convertToKilometers(miles): #Converts miles to kilometers and returns the result
    kilometers = miles * 1.609344 #Formula for converting miles to kilometers
    return kilometers

def checkPlural(value): #Checks whether a value is singular so that a corresponding string can be made plural
    if value != 1:
        return "s"
    else:
        return ""

main() #Executes the main function