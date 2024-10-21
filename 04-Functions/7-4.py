from numer_karty import hide

def main():
    card_number = input("Enter your credit card number (16 digits): ")
    
    try:
        masked_number = hide(card_number)
        
        print("Masked credit card number:", masked_number)
    
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()