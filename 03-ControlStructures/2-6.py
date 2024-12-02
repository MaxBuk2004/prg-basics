number = float(input('Enter number: '))

if number < 0:
    print(f'Number {number} is negative')
elif number == 0:
    print(f'Number {number} is zero')
elif number > 0:
    print(f'Number {number} is positive')