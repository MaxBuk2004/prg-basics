def sum(n):
    if n == 1:
        return 1
    else:
        return n + sum(n - 1)

n = 10
result = sum(n)
print(f"The sum of natural numbers from 1 to {n} is: {result}")