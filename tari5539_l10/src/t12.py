"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Muhammad Talal Tariq
ID:      169035539
Email:   tari5539@mylaurier.ca
__updated__ = "2022-11-15"
-------------------------------------------------------
"""
# imports
from functions import find_shortest

name = "words.txt"
fh = open(name, "r", encoding="utf-8")
print(f"file '{name}' open for reading")
word = find_shortest(fh)
fh.close()
print(f"'{word}' is the first shortest word")
