#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    n = -10
else:
    n = 10
print("Last digit of {} is {} and is".format(number, number % n), end=" ")
if number % 10 > 5:
    print("greater than 5")
else:
    if number % 10 != 0:
        print("less than 6 and not 0")
    else:
        print("0")
