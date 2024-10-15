print('SURVEY:')
x = input('Are you interested in computer science? (y/n):')
y = input('Are you interested in computer science? (y/n):')
z = input('Are you interested in computer science? (y/n):')
if x=='y':
    x = True
else:
    x = False
if y=='y':
    y = True
else:
    y = False
if z=='y':
    z = True
else:
    z = False

print('SURVEY RESULTS:')
print(f'Interested in computer science: {x}')
print(f'Playing computer games: {y}')
print(f'Has an Instagram account: {z}')