from checkbi import f

def main():
    # Test cases
    test_cases = ["101101", "1311a10100", "1001", "0", "1", "0101010101", "110200"]
    
    for binary in test_cases:
        result = f(binary)
        print(f'f("{binary}") returns {result}')

if __name__ == "__main__":
    main()