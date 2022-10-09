#!/usr/bin/python3


def best_score(a_dictionary):

    if not a_dictionary:
        return None

    valueList = a_dictionary.values()
    keyList = a_dictionary.keys()

    maxScore = sorted(valueList)[-1]
    maxScoreHolder = list(keyList)[list(valueList).index(maxScore)]

    return maxScoreHolder
