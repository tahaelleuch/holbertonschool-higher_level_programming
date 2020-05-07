#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return (0)
    sum = 0
    power = 0
    for i in my_list:
        sum = sum + (i[0] * i[1])
        power = power + i[1]
    av = sum / power
    return (av)
