#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Convert arabic number to roman number function."""


def arb_2_rom(arabic_number):
    """Convert arabic number to roman number function."""
    roman_numerals = {
        0: [1000, 'M'],
        1: [900, 'CM'],
        2: [500, 'D'],
        3: [400, 'CD'],
        4: [100, 'C'],
        5: [90, 'XC'],
        6: [50, 'L'],
        7: [40, 'XL'],
        8: [10, 'X'],
        9: [9, 'IX'],
        10: [5, 'V'],
        11: [4, 'IV'],
        12: [1, 'I']
    }
    roman_number = ''
    for key, value in roman_numerals.items():
        while arabic_number >= value[0]:
            roman_number += value[1]
            arabic_number -= value[0]
    return roman_number

arabic_number = 2945
roman_number = arb_2_rom(arabic_number)
print('%s(%s)' % (roman_number, arabic_number))
