#!/usr/bin/python3
def pow(iMultiple, iMultiplier):
    result = iMultiple
    if iMultiplier > 0:
        for i in range(1, iMultiplier):
            result = result * iMultiple
    elif iMultiplier < 0:
        for i in range(0, iMultiplier - 1, -1):
            result = result / iMultiple
    elif iMultiplier == 0:
        result = 1
    return result
