#!/usr/bin/python
def print_last_digit(number):
    if number < 0:
        pos_number = number * -1
    else:
        pos_number = number
    a = pos_number % 10
    print(a, end = '')
    return (a)
