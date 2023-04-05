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
from functions import count_frequency_value

name = "numbers.txt"
fh = open(name, "r", encoding="utf-8")
print(f"file '{name}' open for reading")
value = int(input("Value to count: "))
count = count_frequency_value(fh, value)
fh.close()
print(value, f"appears {count} time(s)")
