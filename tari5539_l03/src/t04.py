"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Muhammad Talal Tariq
ID:      169035539
Email:   tari5539@mylaurier.ca
__updated__ = "2022-09-26"
-------------------------------------------------------
"""
price = float(input("Enter number: "))
percent = float(input("Enter percent: "))
discount = price * (percent / 100)
print(f"A {percent} percent discount on {price:.1f} is {discount:.1f}")
