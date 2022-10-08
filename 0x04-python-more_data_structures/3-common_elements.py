#!/usr/bin/python3


def common_elements(set_1, set_2):

    commonElements = set()
    firstSetLength = len(set_1)
    secondSetLength = len(set_2)

    if firstSetLength > secondSetLength:
        countingSet = set_1
        subSet = set_2
    else:
        countingSet = set_2
        subSet = set_1

    for currentItem in countingSet:

        if currentItem in subSet:
            commonElements.add(currentItem)

    return commonElements
