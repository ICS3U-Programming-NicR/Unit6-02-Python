#!/usr/bin/env python3.10

# Created by: Nic Riscalas
# Created on: May 2022
# This program shows the user the largest number between 10 random numbers

import random
import constants


def largest_number(list_of_numbers):
    # this functions figures out the largest number

    biggest_i = 0

    for i in range(0, len(list_of_numbers)):
        if list_of_numbers[i] > list_of_numbers[biggest_i]:
            biggest_i = i

    return biggest_i


def main():
    # this function uses a list

    random_numbers = []

    # input
    for i in range(0, constants.MAX_ARRAY_SIZE):
        single_random_number = random.randint(constants.MIN_NUM, constants.MAX_NUM)
        random_numbers.append(single_random_number)
        print("The random number {0} is {1} ".format(i + 1, single_random_number))

    # call functions
    biggest_index = largest_number(random_numbers)
    # output
    print("The largest number is: {} ".format(random_numbers[biggest_index]))


if __name__ == "__main__":
    main()
