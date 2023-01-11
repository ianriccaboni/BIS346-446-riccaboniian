# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 09:53:27 2023

@author: ianri
"""

ALPHABET = 'abcdefghijklmnopqrstuvwxyz'

def summarize_letters(string):
    letters = []
    counts = []
    
    for letter in string.lower():
        if letter in ALPHABET:
            if letter in letters:
                index = letters.index(letter)
                counts[index] += 1
            else:
                letters.append(letter)
                counts.append(1)
           
    tuples = list(zip(letters, counts))
    tuples.sort()
    return tuples

sentence = 'Zap the Fox Quickly Bounces and Jumps Around For Very Green Ice Cream with Friends'
summary = summarize_letters(sentence)

# display counts
for char, count in summary:
    print(f'{char}: {count}')

# check if all letters of the alphabet were found in the string
all_letters = True

if len(summary) == len(ALPHABET):
    for item in summary:
        if item[0] not in ALPHABET:
            all_letters = False
            break  
else:
    all_letters = False

if all_letters:
    print(f'"{sentence}" contains all the letters in the alphabet')
else:
    print(f'"{sentence}" does not contain all the letters in the alphabet')