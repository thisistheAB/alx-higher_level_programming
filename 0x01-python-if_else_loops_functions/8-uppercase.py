#!/usr/bin/python3
def uppercase(iString):
    for i in iString:
        if 97 <= ord(i) <= 122:
            print('{:c}'.format(ord(i) - 32), end='')
        else:
            print(i, end='')
    print('\n', end='')
