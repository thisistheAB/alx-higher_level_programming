#!/usr/bin/python3


def print_sorted_dictionary(a_dictionary):

    for currentItem in sorted(a_dictionary.keys()):
        print(currentItem, ": ", a_dictionary[currentItem], end="\n", sep="")
