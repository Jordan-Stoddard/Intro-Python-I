"""
The Python standard library's 'calendar' module allows you to 
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `calendar.py month [year]`
and does the following:
 - If the user doesn't specify any input, your program should 
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that 
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.
"""


import sys
import calendar
from datetime import datetime


def getDate(num1=None, num2=None):
    if num1 > 12 or num1 < 1:
        return print('First entry must be greater than 0 and less than 13')
    if type(num1) == int and num2 is None:
        return print(calendar.month(2019, num1))
    if type(num1) == str or type(num2) == str:
        return print('Entries must be valid numbers.')
    if type(num1) == bool or type(num2) == bool:
            return print('Entries must be valid numbers.')
    if type(num1) == int and type(num2) == int:
        return print(calendar.month(num2, num1))
    else:
        return print(calendar.month(2019, datetime.today().month))

print(getDate(0, 1998))
