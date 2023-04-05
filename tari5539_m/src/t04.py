"""
-------------------------------------------------------
Midterm B Task 4 Testing
-------------------------------------------------------
Author: Talal Tariq
ID:     169035539
Email:  tari5539@mylaurier.ca
__updated__ = "2022-11-02"
-------------------------------------------------------
"""
# Imports
from t04_functions import yes_no
# your testing code here
# Do you like cars?(Y/N) Y
# You have good taste

# must ask user to input test values
response = input("Do you like cars?(Y/N) ")
result = yes_no(response)
if result == "Yes":
    print("You have good taste")
elif result == "No":
    print("I do not like you")
else:
    print("Error")
