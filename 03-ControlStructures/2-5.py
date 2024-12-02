###
# Calculates and displays the quarter of the year for a given
# month number (1..12)
#
month = int(input('Enter month number (1, 2..12): '))

if month in range(10, 13): 
    quarter = 4
elif month in range(7, 10): 
    quarter = 3
elif month in range(4, 7): 
    quarter = 2
elif month in range(1, 4):  
    quarter = 1
else:
    quarter = 'Invalid month'

print(f'Month {month} is in quarter {quarter}')