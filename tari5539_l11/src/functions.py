"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Muhammad Talal Tariq
ID:      169035539
Email:   tari5539@mylaurier.ca
__updated__ = "2022-11-16"
-------------------------------------------------------
"""
# imports
from random import randint
# task2


def generate_matrix_char(rows, cols):
    """
    -------------------------------------------------------
    Generates a 2D list of random lower case letter ('a' - 'z') values
    Use: matrix = generate_matrix_char(rows, cols)
    -------------------------------------------------------
    Parameters:
        rows - number of rows in the generated matrix (int > 0)
        cols - number of columns in the generated matrix (int > 0)
    Returns:
        matrix - a 2D list of random characters (2D list of str)
    -------------------------------------------------------
    """
    LETTERS = "abcdefghijklmnopqrstuvwxyz"
    matrix = [[] * cols] * rows

    for i in range(0, rows):
        currentrow = []
        for j in range(0, cols):
            g = randint(0, 25)
            currentrow.append(LETTERS[g])
        matrix[i] = (currentrow)
    return matrix
# task4


def print_matrix_char(matrix):
    """
    -------------------------------------------------------
    Prints the contents of a 2D list of strings in a formatted table.
    Prints row and column headings.
    Use: print_matrix_char(matrix)
    -------------------------------------------------------
    Parameters:
        matrix - a 2D list of strings (2D list)
    Returns:
        None.
    -------------------------------------------------------
    """
    rows = len(matrix)
    cols = len(matrix[0])
    # print header
    print("  ", end="")
    for a in range(0, cols):
        print(f"    {a}", end="")
    print()
    # print rows
    for i in range(0, rows):
        print(f" {i}", end="")
        for j in range(0, cols):
            print(f"    {matrix[i][j]}", end="")
        print()
    return
# task5


def words_to_matrix(word_list):
    """
    -------------------------------------------------------
    Generates a 2D list of character values from the given
    list of words. All words must be the same length.
    Use: matrix = words_to_matrix(word_list)
    -------------------------------------------------------
    Parameters:
        word_list - a list containing the words to be placed in
            the matrix (list of string)
    Returns:
        matrix - a 2D list of characters of the given words
         in word_list (2D list of string).
    -------------------------------------------------------
    """
    rows = len(word_list)
    cols = len(word_list[0])
    matrix = [[] * cols] * rows
    for i in range(0, rows):
        currentrow = []
        for j in range(0, cols):
            currentrow.append(word_list[i][j])
        matrix[i] = currentrow
    return matrix
# task 11


def find_word_vertical(matrix, word):
    """
    -------------------------------------------------------
    Look for word in each column of the given matrix of characters.
    Returns a list of indexes of all column that are equal to word.
    Returns an empty list if no column is equal to word.
    Use: cols = find_word_vertical(matrix, word)
    -------------------------------------------------------
    Parameters:
        matrix - the matrix of characters (2D list of str)
        word - the word to search for (str)
    Returns:
        cols - a list of column indexes (list of int)
    ------------------------------------------------------
    """
    rows = len(matrix)
    colms = len(matrix[0])  # columns, not to be confused w/ the return value
    cols = []

    for j in range(0, colms):
        match = False
        for i in range(0, rows):
            if rows == 1 and matrix[i][j] == word[i]:
                match = True
            if i == rows - 1 and match is True:
                cols.append(j)
            if matrix[i][j] == word[i]:
                match = True

    return cols
# task12


def find_word_diagonal(matrix, word):
    """
    -------------------------------------------------------
    Returns whether word is on the diagonal of a square matrix
    of characters.
    Use: found = find_word_diagonal(matrix, word)
    -------------------------------------------------------
    Parameters:
        matrix - a 2d list of characters (2d list of str)
        word - the word to compare against the diagonal of matrix (str)
    Returns:
        found - True if word is on the diagonal of matrix,
            False otherwise (boolean)
    ------------------------------------------------------
    """
    found = False
    rows = len(matrix)
    for s in range(0, rows):
        if matrix[s][s] == word[s]:
            found = True
        else:
            found = False
            break
    return found
