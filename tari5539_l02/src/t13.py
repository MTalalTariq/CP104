"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Muhammad Talal Tariq
ID:      169035539
Email:   tari5539@mylaurier.ca
__updated__ = "2022-09-20"
-------------------------------------------------------
"""
midmark = float(input("Midterm mark (%): "))
exammark = float(input("Exam mark (%): "))
MWEIGHT = 0.35
EWEIGHT = 0.65
final = midmark * MWEIGHT + EWEIGHT * exammark
print("Final Grade (%):", final)
