def separate_even_odd(array):
    even_numbers = []
    odd_numbers = []
    
    for num in array:
        if num % 2 == 0:
            even_numbers.append(num)
        else:
            odd_numbers.append(num)
    
    return even_numbers + odd_numbers

array = [7, 2, 4, 3, 8, 5, 6, 1, 9, 10]

result = separate_even_odd(array)

print("Original array:", array)
print("Array with even numbers first:", result)