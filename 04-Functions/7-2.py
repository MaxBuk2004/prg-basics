from text import count_letter

def main():
    text = "You never get a second chance to make a first impression"
    
    letter_to_count = 'e'
    
    count = count_letter(text, letter_to_count)
    
    print(f"The number of letter '{letter_to_count}': {count}")

if __name__ == "__main__":
    main()