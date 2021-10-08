#!/usr/bin/python3
def print_last_digit(number):
    """Print the last digit of number, followed by a newline"""
    if number < 0:
        last_digit = -number % 10
    else:
        last_digit = number % 10
    print('{:d}'.format(last_digit), end='')
    return last_digit
