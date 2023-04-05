"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Muhammad Talal Tariq
ID:      169035539
Email:   tari5539@mylaurier.ca
__updated__ = "2022-11-18"
-------------------------------------------------------
"""


# task2
def url_categorize(url):
    """
    -------------------------------------------------------
    Returns whether a url represents a business, a non-profit, or another
    type of organization.
    Use: url_type = url_categorize(url)
    -------------------------------------------------------
    Parameters:
        url - the web address of the organization (str)
    Returns:
        url_type - the organization type (str)
            'business' if url ends with 'com'
            'non-profit' if url ends with 'org'
            'other' if url ends with something else
    ------------------------------------------------------
    """
    length = len(url)
    url_type = "other"
    if url[length - 3:length] == 'com':
        url_type = "business"
    elif url[length - 3:length] == 'org':
        url_type = "non-profit"
    else:
        url_type = "other"
    return url_type
# task4


def validate_code(product_code):
    """
    -------------------------------------------------------
    Parses a given product code and prints whether the various parts are valid.
    A product code has three parts:
        The first three letters describe the product category and must
        all be in upper case.
        The next four digits are the product ID.
        The remaining characters describe the product's qualifiers,
        such as colour, size, etc. and always begins with an uppercase letter.
    Use: category, digits, qualifiers = validate_code(product_code)
    -------------------------------------------------------
    Parameters:
        product_code - a product code (str)
    Returns:
        category - True if three upper-case characters, False otherwise
        digits - True if four digits, False otherwise
        qualifiers - True if starts with 1 upper-case letter, False otherwise
    -------------------------------------------------------
    """
    category = False
    digits = False
    qualifiers = False
    length = len(product_code)
    if length >= 3:
        if product_code[0:3].isupper() == True:
            category = True

    if length >= 7:
        if product_code[3:7].isdigit() == True:
            digits = True

    if length >= 8:
        if product_code[7].isupper() == True:
            qualifiers = True

    return category, digits, qualifiers
# task7


def vowel_count(s):
    """
    -------------------------------------------------------
    Counts the number of vowels in a string. Does not include 'y'.
    Use: count = vowel_count(s)
    -------------------------------------------------------
    Parameters:
        s - a string (str)
    Returns:
        count - the number of vowels in s (int)
    -------------------------------------------------------
    """
    VOWELS = ["a", "A", "e", "E", "i", "I", "o", "O", "u", "U"]
    count = 0
    for c in VOWELS:
        count += s.count(c)

    return count
# task10


def text_analyze(txt):
    """
    -------------------------------------------------------
    Analyzes txt and returns the number of uppercase letters,
    lowercase letters, digits, and number of whitespaces in txt.
    Use: uppr, lowr, dgts, whtspc = text_analyze(txt)
    -------------------------------------------------------
    Parameters:
        txt - the text to be analyzed (str)
    Returns:
        uppr - number of uppercase letters in txt (int >= 0)
        lowr - number of lowercase letters in txt (int >= 0)
        dgts - number of digits in txt (int >= 0)
        whtspc - number of white spaces in the text (spaces, tabs, linefeeds) (int >= 0)
    ------------------------------------------------------
    """

    uppr = 0
    lowr = 0
    dgts = 0
    whtspc = 0
    UP = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
          "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    LO = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
          "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    DI = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", ]
    WH = " "
    for a in range(0, 26):
        uppr += txt.count(UP[a])
    for b in range(0, 26):
        lowr += txt.count(LO[b])
    for c in range(0, 10):
        dgts += txt.count(DI[c])
    whtspc = txt.count(WH)
    return uppr, lowr, dgts, whtspc
# task12


def comma_period_replace(string):
    """
    -------------------------------------------------------
    Replaces all the commas with a period in s.
    Use: out = comma_period_replace(string)
    -------------------------------------------------------
    Parameters:
        string - a string (str)
    Returns:
        out - string with all commas replaced by a period (str)
    ------------------------------------------------------
    """

    out = ""
    length = len(string)
    for c in range(0, length):
        if string[c] == ",":
            out += "."
        else:
            out += string[c]
    return out
