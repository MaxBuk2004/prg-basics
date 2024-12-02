first = 0
second = 1

print(first, end=' ')
print(second, end=' ')

for i in range(18):  
    next = first + second 
    print(next, end=' ')
    first = second
    second = next

print()