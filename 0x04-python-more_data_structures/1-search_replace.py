#!/usr/bin/python3


def search_replace(my_list, search, replace):

    replacedList = []

    for currentElement in my_list:
        appendElement = currentElement
        if currentElement == search:
            appendElement = replace
        replacedList.append(appendElement)

    return replacedList
