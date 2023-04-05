"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Muhammad Talal Tariq
ID:      169035539
Email:   tari5539@mylaurier.ca
__updated__ = "2022-11-13"
-------------------------------------------------------
"""
# imports
from functions import customer_by_id

print("Find customer by id_number")
id_number = input("Enter an ID: ")
name = "customers.txt"
fh = open(name, "r", encoding="utf-8")
result = customer_by_id(fh, id_number)
fh.close()
print(result)
