def bubblesort(array):
    n = len(array)
    for i in range(n):
        for j in range(0, n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array

arrays = [
    [64, 34, 25, 12, 22, 11, 90],
    [5, 1, 4, 2, 8],
    [3, 0, -1, 8, 7, 2]
]

for index, arr in enumerate(arrays, start=1):
    print(f"Original Array {index}: {arr}")
    sorted_arr = bubblesort(arr[:])
    print(f"Sorted Array {index}: {sorted_arr}")
    print("-" * 30)