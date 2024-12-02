###
# Program for testing built-in functions
#
max_number = max(7,5,6,3,8,2)
print('Max number of 7,5,6,3,8,2 is', max_number)

min_number = min(4,7,2,3,9,8)
print('Min number of 4,7,2,3,9,8 is', min_number)

str_length = len("computer science")
print('The number of characters in "computer science" is', str_length)

letter = input("Enter a letter: ")
print(f"Letter entered: {letter}")

number_from_string = int("20303")
print(f"Number representing the string '20303' is: {number_from_string}")

binary_representation = bin(304)
print(f"Binary representation of 304: {binary_representation}")

hexadecimal_representation = hex(304)
print(f"Hexadecimal representation of 304: {hexadecimal_representation}")

unicode_euro = ord('€')
print(f"Unicode code of the € sign: {unicode_euro}")

absolute_value = abs(-17)
print(f"Absolute value of -17: {absolute_value}")