def caesar_decrypt(ciphertext, shift):
    decrypted_text = ''
    for char in ciphertext:
        if char.isalpha():  # check if character is a letter
            shifted = ord(char) - shift
            if char.islower():
                if shifted < ord('a'):
                    shifted += 26
            elif char.isupper():
                if shifted < ord('A'):
                    shifted += 26
            decrypted_text += chr(shifted)
        else:
            decrypted_text += char
    return decrypted_text

encrypted_message = "ge4wiv_jYr"
shift = 4
decrypted_message = caesar_decrypt(encrypted_message, shift)
print("Decrypted message:", decrypted_message)
