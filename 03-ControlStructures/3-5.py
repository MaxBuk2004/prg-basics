###
# Calculates the number of days in a month
#

month = int(input('Enter month number (1..12): '))

if month in [1, 3, 5, 7, 8, 10, 12]:
    days = 31  # Months with 31 days
elif month in [4, 6, 9, 11]:
    days = 30  # Months with 30 days
elif month == 2:
    days = 28  # February has 28 days
else:
    days = 'Invalid month'

if days != 'Invalid month':
    print(f'Month {month} has {days} days.')
else:
    print('Invalid month entered.')