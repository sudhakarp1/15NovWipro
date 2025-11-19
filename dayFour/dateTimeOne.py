'''
import datetime
todayDate = datetime.date.today()
print(todayDate)
print(todayDate.year)
print(todayDate.month)
print(todayDate.day)

import datetime
now = datetime.time(12,48,55)
print(now)

import calendar
print(calendar.month(2025, 11))
print(calendar.weekday(2025, 5, 1))
'''

import datetime
todayDate = datetime.datetime.now()
print(todayDate)
print(todayDate.strftime('%H:%M:%S'))
print(todayDate.strftime('%d/%m/%Y'))
print(todayDate.strftime('%d-%b-%Y'))
print(todayDate.strftime('%d-%B-%Y'))
print(todayDate.strftime('%d-%B-%y'))
#=========================================
