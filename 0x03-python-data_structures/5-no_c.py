#!/usr/bin/python3


def no_c(my_string):

    inputList = list(my_string)
    resultString = ""

    for counter in inputList:
        if 'c' in inputList:
            inputList.remove('c')
        if 'C' in inputList:
            inputList.remove('C')
        if counter != 'C' and counter != 'c':
            resultString = resultString + counter

    return resultString
