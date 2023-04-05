"""
-------------------------------------------------------
Midterm B Task 2 Function Definitions
-------------------------------------------------------
Author: Talal Tariq
ID:     169035539
Email:  tari5539@mylaurier.ca
__updated__ = "2022-11-02"
-------------------------------------------------------
"""


def comic_condition(rating):
    """
    -------------------------------------------------------
    Determines the condition condition given an Air Quality Index (rating).
        If rating is 9.0 or greater, the condition is "near mint".
        If rating is 5.5 or greater but less than 9.0, the condition is "fine".
        If rating is 3.0 or greater but less than 5.5, the condition is "good".
        If rating is 1.5 or greater but less than 3.0, the condition is "fair".
        If rating is 0 or greater but less than 1.5 the condition is "poor".
        If rating is less than 0, return "Error"
    Use: condition = comic_condition(rating)
    -------------------------------------------------------
    Parameters:
        rating - air quality index (int >= 0)
    Returns‌​‌​​​​‌​​‌‌​‌​​​‌‌‌​​​‌​​‌‌:
        condition - description of comic book condition (str)
    -------------------------------------------------------
    """

    # your code here
    condition = ""
    if rating >= 9:
        condition = "near mint"
    elif rating >= 5.5:
        condition = "fine"
    elif rating >= 3:
        condition = "good"
    elif rating >= 1.5:
        condition = "fair"
    elif rating >= 0:
        condition = "poor"
    else:
        condition = "Error"
    return condition
