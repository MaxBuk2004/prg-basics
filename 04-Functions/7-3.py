from range import is_within_range

def main():
    number = int(input("A number: "))
    x = int(input("Range start: "))
    y = int(input("Range end: "))
    
    result = is_within_range(number, x, y)
    
    if result:
        print(f"Number {number} in the range <{x}, {y}>: yes")
    else:
        print(f"Number {number} in the range <{x}, {y}>: no")

if __name__ == "__main__":
    main()