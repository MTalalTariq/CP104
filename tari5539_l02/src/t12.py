"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Muhammad Talal Tariq
ID:      169035539
Email:   tari5539@mylaurier.ca
__updated__ = "2022-10-01"
-------------------------------------------------------
"""
rawinput = int(input("Number of seconds: "))
days = int(rawinput / 86400)
rawinput -= (days * 86400)
hours = int(rawinput / 3600)
rawinput = rawinput - (hours * 3600)
mins = int(rawinput / 60)
rawinput = rawinput - (mins * 60)
secs = rawinput
MIN = 60
print("Days:", days, "Hours:", hours, " Minutes:", mins, " Seconds:", secs)
