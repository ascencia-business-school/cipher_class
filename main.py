def caesar_cipher_encrypt(text, shift):
    """
    Encrypts the given text using the Caesar cipher technique.
    """
    encrypted_text = []
    #Loop through each characters in the text
    for char in text:
        # Check if the character is an alpher numeric character
        if char.isalpha(): 
            # Get the integer value for the ASCII unicode of the Uppercase "A" and "a" only if the character is either uppercase or lowercase
            start = ord('A') if char.isupper() else ord('a')
            new_char = chr((ord(char) - start + shift) % 26 + start)
            encrypted_text.append(new_char)
        else:
            encrypted_text.append(char)
    
    return ''.join(encrypted_text)



text = "Hello, World!"
shift = 3
encrypted = caesar_cipher_encrypt(text, shift)
print("Encrypted Text:", encrypted)
re_encrypted = caesar_cipher_encrypt(encrypted, -3)
print("DE-Encrypted Text:", re_encrypted)
