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
from functions import generate_matrix_char
rows = 3
cols = 5
matrix = generate_matrix_char(rows, cols)
print(matrix)
# print 2 dimentionally
"""
for i in range(0, rows):
    for j in range(0, cols):
        print(matrix[i][j], end=" ")
    print()
"""
