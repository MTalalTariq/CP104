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
from functions import text_analyze
uppr, lowr, dgts, whtspc = text_analyze(" 123Hound 2SPc")
print(f"{uppr}, {lowr}, {dgts}, {whtspc}")
