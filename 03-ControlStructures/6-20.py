amount = int(input('Enter the number of zlotych: '))
one = 0
two = 0
five = 0

five = amount // 5
remaining = amount % 5 
two = remaining // 2 
one = remaining % 2  

print('The amount of PLN 18 in coins:')
print(f'1 PLN coins: {one}')
print(f'2 PLN coins: {two}')
print(f'5 PLN coins: {five}')