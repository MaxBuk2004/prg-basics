def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def f(n):
    count = 0
    current_number = 1
    prime = 0
    
    while count < n:
        current_number += 1
        if is_prime(current_number):
            count += 1
            prime = current_number
            
    return prime

if __name__ == "__main__":
    print(f(1))
    print(f(5))
    print(f(10))