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
from functions import meal_costs
b_total, l_total, s_total, a_total = meal_costs()
print(f"({b_total:.2f}, {l_total:.2f}, {s_total:.2f}, {a_total:.2f})")
