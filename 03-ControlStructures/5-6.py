###
# Calculates the sum of even numbers from 1 to a given number N
#
N = int(input('Enter number N: '))
sum_even = 0
x = 1

# Calculate the sum of even numbers
while x <= N:
    if  x % 2 == 0:
        sum_even += x
    x += 1

print(f"The sum of even numbers from 1 to {N} is: {sum_even}")