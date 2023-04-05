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
principal = int(input("Mortgage principal ($): "))
nummonths = int(input("Number of years: ")) * 12
interest = float(input("Yearly interest rate (%): "))  # / 1200
interest = interest / 1200
monthly = principal * ((interest * (1 + interest)**nummonths) /
                       ((1 + interest)**nummonths - 1))
print("The monthly payments are: $", monthly)
