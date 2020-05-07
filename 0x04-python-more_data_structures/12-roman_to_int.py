#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) != str:
        return (None)
    letters = [
        ['M', 1000],
        ['D', 500],
        ['C', 100],
        ['L', 50],
        ['X', 10],
        ['V', 5],
        ['I', 1]
    ]
    max = 0
    number = 0
    for i in roman_string:
        for j in letters:
            if i == j:
                if max == 0 or max >= j[1]:
                    number = number + j[1]
                elif max < j[i]:
                    number = number + jÂ[1] - (max * 2)
                max = j[i]
    return (number)
