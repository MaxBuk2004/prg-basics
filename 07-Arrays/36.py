def flatten_2d_array(array_2d):
    return [item for row in array_2d for item in row]

def display_1d_array(array_1d):
    print(" ".join(map(str, array_1d)))

arrays_2d = [
    [[2, 3], [1, 5]],
    [[5, 0, 3, 7, 5], [9, 0, 9, 1, 2]],
    [[2, 1], [3, 5], [7, 4], [2, 6]]
]

for idx, array_2d in enumerate(arrays_2d, 1):
    print(f"2D Array {idx}:")
    display_1d_array(flatten_2d_array(array_2d))
    print()