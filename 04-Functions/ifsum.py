def f(number, even):
    number = abs(number)
    
    digit_str = str(number)
    total_sum = 0
    
    for char in digit_str:
        digit = int(char)
        if even:
            if digit % 2 == 0:
                total_sum += digit
        else:
            if digit % 2 != 0:
                total_sum += digit

    return total_sum