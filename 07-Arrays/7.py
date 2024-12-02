arr = [15, 8, 31, 47, 2, 19]

print("Array:", " ".join(map(str, arr)))

sum_of_elements = 0
index = 0

while index < len(arr):
    sum_of_elements += arr[index]
    index += 1

arithmetic_mean = sum_of_elements / len(arr)

print("Arithmetic mean:", arithmetic_mean)