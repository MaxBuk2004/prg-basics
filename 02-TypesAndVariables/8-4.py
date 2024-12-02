###
# A program that reads a SWIFT code from the keyboard
# and displays the bank code and country code.
#
swift = str(input('Podaj kod SWIFT:'))
print(f'Bank Code: {swift[:4]}')
print(f'Country Code: {swift[4:6]}')