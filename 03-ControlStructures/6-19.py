decimal_number = int(input("Enter a decimal number: "))

original_number = decimal_number

binary_number = ''

if decimal_number == 0:
    binary_number = '0'
else:
    while decimal_number > 0:
        remainder = decimal_number % 2  
        binary_number = str(remainder) + binary_number  
        decimal_number = decimal_number // 2  

# Display the result
print(f"{original_number}(10) = {binary_number}(2)")