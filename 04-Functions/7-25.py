def f(product_code):
    if len(product_code) != 4 or not product_code.isdigit():
        return False
    
    first_digit = int(product_code[0])
    second_digit = int(product_code[1])
    third_digit = int(product_code[2])
    
    control_digit = int(product_code[3])
    
    sum = first_digit + second_digit + third_digit
    
    expected_control_digit = sum % 7
    
    return expected_control_digit == control_digit

if __name__ == "__main__":
    print(f("1082"))
    print(f("2035"))
    print(f("1114"))
    print(f("7071"))