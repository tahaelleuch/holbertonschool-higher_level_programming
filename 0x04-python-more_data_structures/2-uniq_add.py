#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq_list = []
    for i in my_list:
        if i not in uniq_list:
            uniq_list.append(i)
    sum = 0
    for j in uniq_list:
        sum = sum + j
    return(sum)
