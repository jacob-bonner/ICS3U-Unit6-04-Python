#!/usr/bin/env python3

# Created by: Jacob Bonner
# Created on: September 2019
# This program calculates the average of an array of numbers


import random


def calculate(list_of_numbers):
    # This function calculates the average of all numbers in a 2D array

    # Variables
    average_divider = 0
    sum_of_numbers = 0

    # Process
    for row_value in list_of_numbers:
        for counter in row_value:
            sum_of_numbers = sum_of_numbers + counter
            average_divider += 1

    number_average = sum_of_numbers/average_divider
    return number_average


def main():
    # This function generates random numbers then prints the average

    # Variables and lists
    number_list = []

    # Input
    rows = int(input("How many random number lists would you like? "))
    columns = int(input("How many numbers in each list? "))
    print("")

    # Process
    for counter in range(0, rows):
        temporary_column = []
        print("Row {0}:".format(counter + 1))
        for counter in range(0, columns):
            random_number = random.randint(0, 50)
            temporary_column.append(random_number)
            print(random_number)
        number_list.append(temporary_column)
        print("")

    average = calculate(number_list)

    # Output
    print("The average of all the numbers is", average)


if __name__ == "__main__":
    main()
