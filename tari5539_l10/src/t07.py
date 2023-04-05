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
from functions import append_max_num

name = "numbers.txt"
fh = open(name, "a+", encoding="utf-8")
print(f"file '{name}' open for reading and writing")
num = append_max_num(fh)
fh.close()
print(num, "is appended")
