#Daniel Preller, 5 June 2025, Assignment 1.3
#Program to print the "bottles of beer on the wall" song with a specified number of bottles

def main():# Main function
    print_bottles(get_bottles())
    print("It's time to buy more bottles of beer.")

def get_bottles():# Gets and verifies number of bottles of beer from the user
    while True:
        try:
            bottles = int(input("Please enter the number of bottles of beer on the wall: "))

            if bottles > 0:
                break
            else:
                raise ValueError

        except ValueError:
            print("Please enter a number greater than 0.")

    return bottles

def print_bottles(bottles):# Prints the lines of the song, correctly handling plurals
    print()# Blank line
    if bottles == 1:
        plural_ending = ""
    else:
        plural_ending = "s"

    while bottles > 0:
        print(f"{bottles} bottle{plural_ending} of beer on the wall, {bottles} bottle{plural_ending} of beer.")
        bottles -= 1

        #Only checks for 0 and 1 because they are the only values that could require a change in plural ending
        if bottles == 1:
            plural_ending = ""
        elif bottles == 0:
            plural_ending = "s"

        print(f"Take one down, pass it around, {bottles} bottle{plural_ending} of beer on the wall\n")

if __name__ == '__main__':# Conditionally executes the main function
    main()