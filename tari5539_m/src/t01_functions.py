"""
-------------------------------------------------------
Midterm B Task 1 Function Definitions
-------------------------------------------------------
Author: Talal Tariq
ID:     169035539
Email:  tari5539@mylaurier.ca
__updated__ = "2022-11-02"
-------------------------------------------------------
"""
# Constants
PENNY = 1
TWOPEN = 2
FIVEPEN = 5
TENPEN = 10
# your code here


def total_coins(pennies, two_pence, five_pence, ten_pence):
    """
    -------------------------------------------------------
    Determines total amount of money in coins in cents.
        1 penny coin = 1 pence
        1 two pence coin = 2 pence
        1 five pence coin = 5 pence
        1 ten pence coin = 10 pence
    Use: total = total_coins(penny, two_pence, five_pence, ten_pence)
    -------------------------------------------------------
    Parameters:
        pennies - number of penny coins (int >= 0)
        two_pence - number of two pence coins (int >= 0)
        five_pence - number of five pence coins (int >= 0)
        ten_pence - number of ten pence coins (int >= 0)
    Returns‌​‌​​​​‌​​‌‌​‌​​​‌‌‌​​​‌​​‌‌:
        total - total value of coins in pence (int)
    -------------------------------------------------------
    """
    total = (pennies * PENNY) + (two_pence * TWOPEN) + \
        (five_pence * FIVEPEN) + (ten_pence * TENPEN)
    # your code here

    return total
