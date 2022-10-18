#!/usr/bin/python3


def roman_to_int(roman_string):

    if not roman_string:
        return 0

    regularRomanDictionary = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    subtractiveRomanDictionary = {"IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900}
    subtractiveIndexes = dict()

    inputLength = len(roman_string)
    decimalNumber = 0

    for subtractiveItemIndex in range(0, inputLength):
        if subtractiveItemIndex == inputLength - 1:
            break
        subtractiveCheck = roman_string[subtractiveItemIndex] + roman_string[subtractiveItemIndex + 1]
        if subtractiveCheck in subtractiveRomanDictionary:
            subtractiveIndexes[subtractiveItemIndex] = subtractiveCheck

    itemIndex = 0
    while itemIndex < inputLength:
        if itemIndex in subtractiveIndexes:
            subtractiveNumber = subtractiveRomanDictionary[subtractiveIndexes[itemIndex]]
            decimalNumber += subtractiveNumber
            itemIndex += 1
        elif roman_string[itemIndex] in regularRomanDictionary:
            currentDecimalNumber = regularRomanDictionary[roman_string[itemIndex]]
            decimalNumber += currentDecimalNumber
        itemIndex += 1

    return decimalNumber
