#!/usr/bin/python3


def max_integer(my_list=[]):

    if not my_list:
        return None
    else:
        maxValue = 0
        for currentValue in my_list:
            if currentValue > maxValue:
                maxValue = currentValue

        return maxValue

