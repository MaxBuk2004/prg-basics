###
# Encrypts text using Caesar Code, shifting each letter
# in the alphabet right one position
#
plain_text = 'The early bird catches the worm'
encrypted_text = ''

for char in plain_text:
    if char == ' ':
        encrypted_text += char
    else:
        # Read the character's code (use ord())
        x = ord(char)
        # Add one to the character's code
        x += 1
        # Replace new character code with its
        # corresponding character (use chr())
        x = chr(x)
        # Add encrypted character to encrypted text
        encrypted_text += x

print(f'plain_text: {plain_text}')
print(f'encrypted_text: {encrypted_text}')