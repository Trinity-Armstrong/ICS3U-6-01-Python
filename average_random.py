#!/usr/bin/env python3

# Created by: Trinity Armstrong
# Created on: December 2019
# This program calculates the average of an array of 10 random numbers


import random


def main():
    # This function calculates the average of an array of 10 random numbers

    # variables and array declaration
    my_numbers = []
    average = 0

    # Process
    for counter in range(10):
        random_number = random.randint(1, 100)
        my_numbers.append(random_number)
        print(my_numbers[counter])
        average = average + my_numbers[counter]

    average = average/10

    # Output
    print("")
    print("The average of these 10 random numbers is", average)


if __name__ == "__main__":
    main()
