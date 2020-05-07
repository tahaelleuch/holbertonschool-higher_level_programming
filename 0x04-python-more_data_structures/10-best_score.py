#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return (None)
    keys = list(a_dictionary.keys())
    max = keys[0]
    for i in keys:
        if a_dictionary[i] > a_dictionary[max]:
            max = i
    return max
