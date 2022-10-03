#!/usr/bin/python3


def max_integer(my_list=[]):

    if len(my_list) == 0:
        return None

    maxValue = 0
    for currentValue in my_list:
        if currentValue > maxValue:
            maxValue = currentValue

    return maxValue
