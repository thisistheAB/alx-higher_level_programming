#!/usr/bin/python3
import random
number = random.randint(-10, 10)

print(number, " is ", end='', sep='', flush=True)
if number > 0:
    print("positive")
elif number < 0:
    print("negative")
else:
    print("zero")
