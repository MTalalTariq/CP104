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

# task3


def population_growth(target, current, rate):
    """
    -------------------------------------------------------
    Determines the number of years to reach a target population.
    Use: years = population_growth(target, current, rate)
    -------------------------------------------------------
    Parameters:
        target - target population (int > current)
        current - current population (int > 1)
        rate - percent rate of growth (float > 0)
    Returns:
        years - the number of years to reach target population (int)
    -------------------------------------------------------
    """
    years = 0
    rate = rate / 100 + 1
    while current <= target:
        if current == target:
            years = 0
        else:
            years += 1
        current *= rate
    return years
# task5


def positive_statistics():
    """
    -------------------------------------------------------
    Asks a user to enter a series of positive numbers, then calculates
    and returns the minimum, maximum, total, and average of those numbers.
    Stop processing values when the user enters a negative number.
    The first number entered must be positive.
    Use: minimum, maximum, total, average = positive_statistics()
    -------------------------------------------------------
    Returns:
        minimum - smallest of the entered values (float)
        maximum - largest of the entered values (float)
        total - total of the entered values (float)
        average - average of the entered values (float)
    ------------------------------------------------------
    """
    num1 = float(input("First positive value: "))
    # var declarations
    num2 = 0
    maximum = num1
    minimum = num1
    total = num1
    average = 0
    counter = 0

    while num2 >= 0:
        num2 = float(input("Next positive value: "))
        if num2 < minimum and num2 >= 0:
            minimum = num2
        if num2 > maximum:
            maximum = num2
        if num2 > 0:
            total += num2
        counter += 1
        average = total / counter
    return minimum, maximum, total, average
# task7


def meal_costs():
    """
    -------------------------------------------------------
    Asks a user the costs of breakfast, lunch, and supper for each
    day the user was away. Assumes there is at least one day, and
    after entering data for each day asks the user whether they want
    to enter data for another day. Calculates total costs for meals.
    Use: b_total, l_total, s_total, a_total = meal_costs()
    -------------------------------------------------------
    Returns:
        b_total - total breakfasts cost (float)
        l_total - total lunches cost (float)
        s_total - total suppers cost (float)
        a_total - all meals cost (float)
    ------------------------------------------------------
    """
    # var declarations
    b_total = 0
    l_total = 0
    s_total = 0
    a_total = 0
    day = 0
    answer = "Y"

    while answer == "Y":
        day += 1
        print(f"For Day {day}")
        print()
        br = float(input("How much was breakfast? $"))
        b_total += br
        lu = float(input("How much was lunch? $"))
        l_total += lu
        su = float(input("How much was supper? $"))
        s_total += su
        tot = su + br + lu
        print(f"Your total for the day was ${tot:.2f}")
        a_total += tot
        print()
        answer = input("Were you away another day (Y/N)? ")
        print()

    return b_total, l_total, s_total, a_total
# task8


def budget(available):
    """
    -------------------------------------------------------
    Asks a user for a series of expenses in a month. Calculate the
    total expenses and determines whether the user is in "Surplus",
    "Deficit", or "Balanced" status.
    Use: expenses, balance, status = budget(available)
    -------------------------------------------------------
    Parameters:
        available - money currently available (float >= 0)
    Returns:
        expenses - total monthly expenses (float)
        balance - remaining balance (float)
        status - One of (str):
            "Surplus" if user budget is in surplus
            "Deficit" if user budget is in deficit
            "Balanced" if user budget is balanced
    ------------------------------------------------------
    """
    exp = float(input("Enter an expense (0 to quit): $"))
    expenses = exp
    while exp > 0:
        exp = float(input("Enter another expense (0 to quit): $"))
        expenses += exp

    balance = available - expenses

    if balance > 0:
        status = "Surplus"
    elif balance < 0:
        status = "Deficit"
    else:
        status = "Balanced"
    return expenses, balance, status
# task9


def get_int(low, high):
    """
    -------------------------------------------------------
    Asks a user for an integer value between low and high, and
    continues asking until an acceptable value is input.
    Use: value = get_int(low, high)
    -------------------------------------------------------
    Parameters:
        low - the lowest acceptable integer (inclusive) (int)
        high - the higest acceptable integer (inclusive) (int > low)
    Returns:
        value - a number between low and high (int)
    ------------------------------------------------------
    """
    inbounds = False
    value = 0
    while inbounds == False:
        ans = int(input("Enter a value between 0 and high 100: "))
        if ans > high:
            print("Value entered is too high")
        elif ans < low:
            print("Value entered is too low")
        else:
            value = ans
            inbounds = True
    return value
