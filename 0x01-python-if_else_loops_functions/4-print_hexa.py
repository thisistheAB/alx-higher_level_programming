#!/usr/bin/python3
for i in range(0, 99):
    print('{:n}{:s}'.format(i, " = 0x"), end='')
    print('{0:x}'.format(i))
