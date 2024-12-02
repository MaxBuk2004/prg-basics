arr = [15, 8, 31, 47, 2, 19]

print("Array:", " ".join(map(str, arr)))

sum_of_elements = 0

for num in arr:
    sum_of_elements += num

arithmetic_mean = sum_of_elements / len(arr)

print("Arithmetic mean:", arithmetic_mean)