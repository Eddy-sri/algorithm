"""
    eddy <==> [5, 4, 4, 25]
"""

from string import ascii_lowercase

def encoder(str):
    letter = ascii_lowercase
    val = str.lower()
    return [letter.index(char) + 1  for char in val]

def decoder (num_list):
    letter = ascii_lowercase
    return "".join(letter[num-1] for num in num_list)

