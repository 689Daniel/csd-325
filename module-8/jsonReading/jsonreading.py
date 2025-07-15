#Daniel Preller, Assignment 8.2, 15 July 2025
#Program to open JSON file of student information, display it, and add my information

import json

def main():
    with open("students.json", "r") as students_file:# Opens file for writing
        students = json.load(students_file)

        print("Original student list:")
        print_students(students)
        #prints original information

        students.append({"F_Name":"Daniel",
                         "L_Name":"Preller",
                         "Student_ID":79642,
                         "Email":"dpreller@my365.bellevue.edu"})# Adds my information

        print("Updated student list:")
        print_students(students)
        #Prints updated information

    with open("students.json", "w") as students_file:# Opens file again for rewriting to replace original data with updated
        json.dump(students, students_file, indent=4)
        print("The JSON file has been updated.")

def print_students(students_list):# Takes a list of student information dictionaries and formats and prints each student's information
    for student in students_list:
        print(f"{student["L_Name"]}, {student["F_Name"]}: ID = {student["Student_ID"]}, email = {student["Email"]}")
    print("")

if __name__ == '__main__':
    main()