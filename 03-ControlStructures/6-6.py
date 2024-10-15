age = int(input('Enter your age: '))
if age < 13:
    print('Your are a Child')
elif age >= 13 and age <= 19:
    print('Your are a Teen')
elif age >= 20 and age < 64:
   print('Your are a Adult')
elif age >= 65:
   print('Your are a Senior')