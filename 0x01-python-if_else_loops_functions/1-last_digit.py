#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    pos_number = number * -1
else:
    pos_number = number
a = pos_number % 10
print('Last digit of {} is {} '.format(number, a), end='')
if a > 5:
    print('and is greater than 5')
elif a == 0:
    print('and is 0')
else:
    print('and is less than 6 and not 0')
