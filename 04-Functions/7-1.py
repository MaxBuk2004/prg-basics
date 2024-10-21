from month import month

def main():
    month_number = int(input("Enter month number (1-12): "))

    month_name = month(month_number)

    print(f"The name of month {month_number} is {month_name}")

if __name__ == "__main__":
    main()