# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 09:30:39 2023

@author: ianri
"""

alphabet = 'abcdefghijklmnopqrstuvwxyz'

print('first half of the string using starting and ending indices:', alphabet[0:len(alphabet) // 2])

print('first half of the string using only the ending index:', alphabet[:len(alphabet) // 2])

print('second half of the string using starting and ending indices:', alphabet[len(alphabet) // 2:len(alphabet)])

print('second half of the string using only the starting index:', alphabet[len(alphabet) // 2:len(alphabet)])

print('second half of the string using only the ending index:', alphabet[len(alphabet) // 2:])

print("second letter in the string starting with 'a':", alphabet[::2])

print('string in reverse', alphabet[::-1])

print("third letter of the string in reverse starting with 'z'", alphabet[::-3])