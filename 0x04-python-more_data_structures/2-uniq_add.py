#!/usr/bin/python3


def uniq_add(my_list=[]):

    additionResult = 0
    addedItems = []

    for currentItem in my_list:

        if currentItem not in addedItems:
            additionResult += currentItem
            addedItems.append(currentItem)

    return additionResult
