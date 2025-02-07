import random 
import string

char = " " + string.punctuation + string.digits + string.whitespace + string.ascii_letters

char = list(char)
key = char.copy()

print(char)
print(key)

random.choice(key)

plain_letter = input("Enter Your Plain text Number:  ")
decode_text = ""

for letter in char:
    index = char.index(letter)
    decode_text += key[index]
    
print(f"your plain text is: {plain_letter}")
print(f"Your decode Text is: {decode_text}")

print("-------text for visit our website--------")
