###
# Calculates the sum of the digits in a number
#
def sum_digits(number):
    suma = 0
    number = abs(number)
    to_str = str(number)
    for i in to_str:
        suma += int(i)
    return(suma)

any_number = int(input('Enter integer number: '))
result = sum_digits(any_number)
print(f'The sum of the digits in the number {any_number} is {result}')