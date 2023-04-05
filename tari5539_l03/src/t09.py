"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Muhammad Talal Tariq
ID:      169035539
Email:   tari5539@mylaurier.ca
__updated__ = "2022-09-28"
-------------------------------------------------------
"""
sweatband = float(input("Enter sweatband cost: $"))
pants = float(input("Enter pants cost: $"))
jacket = float(input("Enter jacket cost: $"))
print()
total = sweatband + pants + jacket
print("Clothes      Cost")
print(f"Sweatband    ${sweatband:6.2f}")
print(f"Pants        ${pants:6.2f}")
print(f"Jacket       ${jacket:6.2f}")
print(f"Total        ${total:6.2f}")
