pin = str('0805')
x = 0
while x < 3:
    entered_pin = str(input('Podaj PIN: '))
    if entered_pin == pin:
        print('Correct PIN')
        break
    else:
        print('Incorrect PIN')
        x += 1
if x >=3 :
    print('Sorry, your payment card has been blocked.')