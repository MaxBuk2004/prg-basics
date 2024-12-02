hours = int(input('Enter number of hours on the parking: '))
if hours >= 1 and hours <=2:
    print(f'For {hours} hours the fee is 5zl')
elif hours >= 3 and hours <=6:
    print(f'For {hours} hours the fee is 15zl')
elif hours > 6:
    print(f'For {hours} hours the fee is 20zl')