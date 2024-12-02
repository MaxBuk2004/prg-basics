def count_greater_than(array, value):
    count = 0
    for num in array:
        if num > value:
            count += 1
    return count

array = [1.5, 2.8, 3.7, 4.1, 5.9, 0.2, 3.5]

value = float(input("Enter a value: "))

result = count_greater_than(array, value)

print(f"Number of elements greater than {value}: {result}")