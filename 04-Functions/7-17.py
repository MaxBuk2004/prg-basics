def f(number):
    
    str_number = str(number)
    seen = []
    sum_of_repeats = 0

    i = 0
    while i < len(str_number):
        digit = str_number[i]
        if digit in seen:
            sum_of_repeats += int(digit)
        else:
            seen.append(digit)
        i += 1

    return sum_of_repeats

if __name__ == "__main__":
    print(f(1027))
    print(f(230335))
    print(f(513553007))