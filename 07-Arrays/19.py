import MyArrays

arr = [7, 3, 8, 5, 2]

print("Numbers:", MyArrays.array_to_string(arr))

second_largest_number = MyArrays.second_largest(arr)
print(f"Second largest number: {second_largest_number}")

median_value = MyArrays.median(arr)
print(f"Median: {median_value}")

smallest_largest_values = MyArrays.smallest_largest(arr)
print(f"Smallest and largest number: {smallest_largest_values[0]},{smallest_largest_values[1]}")

numbers_as_string = MyArrays.array_to_string(arr)
print(f"Numbers as a string: {numbers_as_string}")