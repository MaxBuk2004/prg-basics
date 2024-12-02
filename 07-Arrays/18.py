my_tuple = (50, 20, 40, 50, 30, 50)

value = int(input("Enter a value to count occurrences: "))

occurrences = my_tuple.count(value)

print("Tuple:", ", ".join(map(str, my_tuple)))
print(f"Value: {value}")
print(f"Number of occurrences: {occurrences}")