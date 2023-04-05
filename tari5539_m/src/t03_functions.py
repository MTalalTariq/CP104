"""
-------------------------------------------------------
Midterm B Task 3 Function Definitions
-------------------------------------------------------
Author: Talal Tariq
ID:     169035539
Email:  tari5539@mylaurier.ca
__updated__ = "2022-11-02"
-------------------------------------------------------
"""
# Constants
BASE = 100.00
XTRA = 40.00
DISC = 10
# your code here


def tire_change():
    """
    -------------------------------------------------------
    Determines the cost of changing tires. The cost is made up of:
        base cost: $100.00
        cost per extra service: $40.00
        Extra Care discount 10% only if:
            more than 1 extra service purchased
            and purchaser is an Extra Care customer
    Use: cost = tire_change()
    -------------------------------------------------------
    Returns‌​‌​​​​‌​​‌‌​‌​​​‌‌‌​​​‌​​‌‌:
        cost - cost of a tire change based upon the base cost,
            the number of extra services purchased, and Extra Care discount
            if applicable (float)
    -------------------------------------------------------
    """

    # your code here
    extranum = int(input("How many extra services are you purchasing? "))
    cost = BASE + (extranum * XTRA)

    if extranum > 1:
        care = input("Are you an Extra Care customer (Y/N)? ")
        if care == "Y":
            cost = cost - (cost * (DISC / 100))
        else:
            cost = cost

    return cost
