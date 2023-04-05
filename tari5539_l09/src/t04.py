"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Muhammad Talal Tariq
ID:      169035539
Email:   tari5539@mylaurier.ca
__updated__ = "2022-11-12"
-------------------------------------------------------
"""
# imports
from functions import validate_code
category, digits, qualifiers = validate_code('BFG9000x7')
print(f"({category}, {digits}, {qualifiers})")
