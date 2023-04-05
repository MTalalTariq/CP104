"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Muhammad Talal Tariq
ID:      169035539
Email:   tari5539@mylaurier.ca
__updated__ = "2022-10-30"
-------------------------------------------------------
"""
# imports
from functions import budget
expenses, balance, status = budget(200)
print()
print(f"({expenses:.2f}, {balance:.2f})")
