"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Muhammad Talal Tariq
ID:      169035539
Email:   tari5539@mylaurier.ca
__updated__ = "2022-11-10"
-------------------------------------------------------
"""
# imports
from random import randint
# constants
WEEK = ["Sunday", "Monday",
        "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
DIGIT = ["zero", "one", "two", "three", "four",
         "five", "six", "seven", "eight", "nine"]
# task1


def get_weekday_name(d):
    """
    -------------------------------------------------------
    Returns the name of a day of the week given its number.
    Use: name = get_weekday_name(d)
    -------------------------------------------------------
    Parameters:
        d - day of week number (1 <= int <= 7)
    Returns:
        name - matching day of the week, 1 = "Sunday", 7 = "Saturday" (str)
    -------------------------------------------------------
    """
    name = 0
    for i in range(0, d):
        name = WEEK[i]
    return name
# task3 (not required)


def get_digit_name(n):
    """
    -------------------------------------------------------
    Returns the name of a digit given its number.
    Use: name = get_digit_name(n)
    -------------------------------------------------------
    Parameters:
        n - digit number (int 0 <= n <= 9)
    Returns:
        name - matching digit, 0 = "zero", 9 = "nine" (str)
    -------------------------------------------------------
    """
    name = 0
    for i in range(0, n + 1):
        name = DIGIT[i]
    return name
# task5


def get_lotto_numbers(n, low, high):
    """
    -------------------------------------------------------
    Generates a sorted list of unique lottery numbers.
    Requires import: from random import randint
    Use: numbers = get_lotto_numbers(n, low, high)
    -------------------------------------------------------
    Parameters:
        n - number of lottery numbers to generate (int > 0)
        low - low value of the lottery number range (int >= 0)
        high - high value of the lottery number range (int > low)
    Returns:
        numbers - a list of unique random lottery numbers (list of int)
    -------------------------------------------------------
    """
    # OG code
    """
    numbers = [0] * n
    for i in range(n):
        numbers[i] = randint(low, high)
    numbers.sort()
    """
    numbers = []
    i = 0
    while i < n:
        temp = randint(low, high)
        if temp not in numbers:
            numbers.append(temp)
        i += 1
    numbers.sort()

    return numbers
# task8


def linear_search(values, value):
    """
    -------------------------------------------------------
    Searches through values for value and returns its index.
    User: index = linear_search(values, value)
    -------------------------------------------------------
    Parameters:
        values - a list of values (list of *).
        value - can be compared to items in values (*).
    Returns:
        index - the index of the location of value in values,
            -1 if not found (int).
    -------------------------------------------------------
    """
    index = -1
    length = len(values)
    test = 0
    while test < length:
        if value == values[test]:
            index = test
            break
        test += 1
    return index
# task10


def min_search(values):
    """
    -------------------------------------------------------
    Searches through values for the minimum value(s) and returns a
    list of the indexes of those values. (Assumes values has at least
    one element.)
    User: indexes = min_search(values)
    -------------------------------------------------------
    Parameters:
        values - a list of values (list of *).
    Returns:
        indexes - a list of indexes of the minimum values in
            values (list of int).
    -------------------------------------------------------
    """
    indexes = []
    length = len(values)
    min = values[0]
    for i in range(length):
        if values[i] < min:
            min = values[i]
            indexes = []
            indexes.append(i)
        elif values[i] == min:
            indexes.append(i)
    return indexes

# task15


def symmetric_difference(source1, source2):
    """
    -------------------------------------------------------
    Returns a list that is the symmetric difference of the contents
    of source1 and source2.
    Only elements that appear in one of source1 and source2, but not both,
    appear once and only once in target.
    Use: target = symmetric_difference(source1, source2)
    -------------------------------------------------------
    Parameters:
        source1 - a list (list of *)
        source2 - a list (list of *)
    Returns:
        target - the symmetric difference of source1 and source2 (list of *)
    -------------------------------------------------------
    """
    target = []
    length1 = len(source1)
    length2 = len(source2)
    # check source1
    for i in range(length1):
        if source1[i] not in source2:
            target.append(source1[i])
    # check source2
    for i in range(length2):
        if source2[i] not in source1:
            target.append(source2[i])
    return target
