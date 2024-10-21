from cash import f

def main():
    test_cases = [23, 8, 2, 0, 11, 15, 3]
    
    for amount in test_cases:
        result = f(amount)
        print(f'f({amount}) returns {result}')

if __name__ == "__main__":
    main()