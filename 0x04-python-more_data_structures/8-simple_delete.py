#!/usr/bin/python3


def simple_delete(a_dictionary, key=""):

    poppedDictionary = a_dictionary

    if key in a_dictionary.keys():
        poppedDictionary.pop(key)

    return poppedDictionary
