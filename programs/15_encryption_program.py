# 44. Encryption Program

import random
import string

chars = string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()

random.shuffle(key)

# print(f"Chars: {chars}")
# print(f"Key: {key}")

# ENCRYPT

plain_text = input("Enter a message to encrypt: ")
cipher_text = ""

for letter in plain_text:
    index = chars.index(letter)
    cipher_text += key[index]

print(f"The plain text is: {plain_text}")
print(f"The cipher text is: {cipher_text}")


# DECRYPT

cipher_text = input("Enter a message to decrypt: ") 
plain_text = ""


for letter in cipher_text:
    index = key.index(letter)
    plain_text += chars[index]

print(f"The cipher text is: {cipher_text}")
print(f"The plain text is: {plain_text}")


