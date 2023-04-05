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
from functions import file_copy_n

name1 = "words.txt"
fh_1 = open(name1, "r", encoding="utf-8")
name2 = "new_words.txt"
fh_2 = open(name2, "a", encoding="utf-8")
print(f"Copying '{name1}' to '{name2}'")
n = int(input("Number of lines to copy: "))
file_copy_n(fh_1, fh_2, n)
fh_1.close()
fh_2.close()
