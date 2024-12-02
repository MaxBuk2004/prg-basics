def is_subset(arr1, arr2):
    for element in arr1:
        if element not in arr2:
            return False
    return True

arr1 = [3, 5, 7]
arr2 = [1, 2, 3, 4, 5, 6, 7]

result = is_subset(arr1, arr2)

if result:
    print(f"Array {arr1} is a subset of array {arr2}.")
else:
    print(f"Array {arr1} is NOT a subset of array {arr2}.")