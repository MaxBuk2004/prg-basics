###
# Counts vowels in the text
#
text = "This is a sample text."
text_length = len(text)
vowels = "aeiouAEIOU"
x = 0
vowel_count = 0

# Count vowels in the text
while x < text_length:
    if text[x] in vowels:
        vowel_count += 1
    x += 1

print(f"The number of vowels in the text is: {vowel_count}")