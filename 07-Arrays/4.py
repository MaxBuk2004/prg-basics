arr = [8, 2, 5, 1, 9]

print("Array:", " ".join(map(str, arr)))

squared_arr = [x**2 for x in arr]

print("2nd power:", " ".join(map(str, squared_arr)))