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
from functions import customer_record
print("Find record n")
n = int(input("Enter a record number: "))
name = "customers.txt"
fh = open(name, "r", encoding="utf-8")
result = customer_record(fh, n)
print(result)

fh.close()
