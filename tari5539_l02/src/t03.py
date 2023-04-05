"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Muhammad Talal Tariq
ID:      169035539
Email:   tari5539@mylaurier.ca
__updated__ = "2022-09-19"
-------------------------------------------------------
"""
bigdogs = int(input("Number of large dogs groomed: "))
smalldogs = int(input("Number of small dogs groomed: "))
BIGDOGPRICE = 75
SMALLDOGPRICE = 50
total = smalldogs * SMALLDOGPRICE + bigdogs * BIGDOGPRICE
print("Total earned for the day: $", total)
