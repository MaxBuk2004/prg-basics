my_tuple = (10, 20, 30, 40, 50)

print("Tuple:", ", ".join(map(str, my_tuple)))

reversed_tuple = my_tuple[::-1]
print("Reverse order:", ", ".join(map(str, reversed_tuple)))