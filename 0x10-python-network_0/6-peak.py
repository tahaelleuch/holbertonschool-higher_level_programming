#!/usr/bin/python3
"""find the peak element on a list"""
def find_peak(list_of_integers):
    """find_peak func
    Args:
        list_of_integers: unsorted list to sheck
    """
    if not list_of_integers:
        return None
    l = list_of_integers
    lenth = len(list_of_integers)
    for e in range(lenth - 1):
        if e == 0:
            continue
        if l[e - 1] < l[e] and l[e + 1] < l[e]:
            return l[e]
    return l[e]
