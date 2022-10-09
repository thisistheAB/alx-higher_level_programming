#!/usr/bin/python3


def multiply_by_2(a_dictionary):

    multipliedDictionary = dict()
    keyList = a_dictionary.keys()

    for currentKey in keyList:
        multipliedDictionary[currentKey] = a_dictionary[currentKey] * 2

    return multipliedDictionary
