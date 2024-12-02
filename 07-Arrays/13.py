def unique_elements(array):
    unique = []
    for num in array:
        if array.count(num) == 1:
            unique.append(num)
    return unique

array = [2, 3, 2, 5, 8, 1, 9, 8]

print("Array:", " ".join(map(str, array)))

unique = unique_elements(array)
print("Unique elements:", " ".join(map(str, unique)))