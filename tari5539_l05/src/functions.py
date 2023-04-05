"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Muhammad Talal Tariq
ID:      169035539
Email:   tari5539@mylaurier.ca
__updated__ = "2022-10-19"
-------------------------------------------------------
"""
from math import fabs
# constants

# task 1


def magic_date(day, month, year):
    """
    -------------------------------------------------------
    Determines if a date is magic. A date is magic if the day
    times the month equals the year.
    Use: magic = magic_date(day, month, year)
    -------------------------------------------------------
    Parameters:
        day - numeric day (int > 0)
        month - numeric month (int > 0)
        year - numeric two-digit year (int > 0)
    Returns:
        magic - True if date is magic, False otherwise (boolean)
    -------------------------------------------------------
    """
    magic = False
    if day * month == year:
        magic = True
    else:
        magic = False
    return magic
# task 4


def closest(target, v1, v2):
    """
    -------------------------------------------------------
    Determines closest value of two values to a target value.
    Use: result = closest(target, v1, v2)
    -------------------------------------------------------
    Parameters:
        target - the target value (float)
        v1 - first comparison value (float)
        v2 - second comparison value (float)
    Returns:
        result - one of v1 or v2 that is closest to target,
          v1 is the value chosen if v1 and v2 are an equal
          distance from target (float)
    -------------------------------------------------------
    """
    dist1 = fabs(target - v1)
    dist2 = fabs(target - v2)
    result = v1
    if dist1 <= dist2:
        result = v1
    else:
        result = v2
    return result
# task 8


def roman_numeral(n):
    """
    -------------------------------------------------------
    Convert 1-10 to Roman numerals.
    Use: numeral = roman_numeral(n)
    -------------------------------------------------------
    Parameters:
        n - number to convert to Roman numerals (int)
    Returns:
        numeral - Roman numeral version of n, None if n is not
          between 1 and 10 inclusive. (str)
    -------------------------------------------------------
    """
    numeral = ""
    if n == 1:
        numeral = "I"
    elif n == 2:
        numeral = "II"
    elif n == 3:
        numeral = "III"
    elif n == 4:
        numeral = "IV"
    elif n == 5:
        numeral = "V"
    elif n == 6:
        numeral = "VI"
    elif n == 7:
        numeral = "VII"
    elif n == 8:
        numeral = "VIII"
    elif n == 9:
        numeral = "IX"
    elif n == 10:
        numeral = "X"
    else:
        numeral = ""
    return numeral
# task 12


def pay_raise(status, years, salary):
    """
    -------------------------------------------------------
    Calculates pay raises for employees. Pay raises are based on:
    status: Full Time ('F)' or Part Time ('P')
    and years of service
    Raises are:
        5% for full time greater than or equal to 10 years service
        1.5% for full time less than 4 years service
        3% for part time greater than 10 years service
        1% for part time less than 4 years service
        2% for all others
    Use: new_salary = pay_raise(status, years, salary)
    -------------------------------------------------------
    Parameters:
        status - employment type (str - 'F' or 'P')
        years - number of years employed (int > 0)
        salary - current salary (float > 0)
    Returns:
        new_salary - employee's new salary (float).
    -------------------------------------------------------
    """
    new_salary = salary
    RAISE1 = 5
    RAISE2 = 1.5
    RAISE3 = 3
    RAISE4 = 1
    RAISE5 = 2
    YEARA = 10
    YEARB = 4
    if status == "F" and years >= YEARA:
        new_salary = salary * (RAISE1 / 100 + 1)
    elif status == "F" and years < YEARB:
        new_salary = salary * (RAISE2 / 100 + 1)
    elif status == "P" and years > YEARA:
        new_salary = salary * (RAISE3 / 100 + 1)
    elif status == "P" and years < YEARB:
        new_salary = salary * (RAISE4 / 100 + 1)
    else:
        new_salary = salary * (RAISE5 / 100 + 1)
    return new_salary

# task 14


def ticket():
    """
    -------------------------------------------------------
    School play ticket price calculation.
    Asks user for their age, and if necessary, if they are
    a student at the school. Prices:
        Infant (age < 3): $0
        Senior (age >= 65): $4.00
        Student (10 <= age < 18): $3.00
            Student of this school: $1.00
        Adult (18 <= age < 65): $5.00
        Kid (3 <= age < 10): $2.00
    Use: price = ticket()
    -------------------------------------------------------
    Returns:
        price - the price of one ticket (float)
    -------------------------------------------------------
    """
    age = int(input("How old are you? "))
    AGE3 = 3
    AGE65 = 65
    AGE10 = 10
    AGE18 = 18

    price = 0
    student = False
    if age < AGE3:
        price = 0
    elif age >= AGE65:
        price = 4
    elif AGE10 <= age < AGE18:
        student = input("Are you a student of the school? ")
        if student == "Y":
            price = 1
        elif student == "N":
            price = 3
    elif AGE18 <= age < AGE65:
        price = 5
    elif AGE3 <= age < AGE10:
        price = 2
    return price
