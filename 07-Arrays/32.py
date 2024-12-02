array = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15]
]

print("Array before swapping:")
for row in array:
    print(row)

array[0], array[2] = array[2], array[0]

print("\nArray after swapping:")
for row in array:
    print(row)