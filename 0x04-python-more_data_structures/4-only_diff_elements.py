#!/usr/bin/python3


def only_diff_elements(set_1, set_2):

    combinedSet = set.union(set_1, set_2)
    uniqueSet = set()

    for currentItem in combinedSet:

        if currentItem not in set_1 or currentItem not in set_2:
            uniqueSet.add(currentItem)

    return uniqueSet
