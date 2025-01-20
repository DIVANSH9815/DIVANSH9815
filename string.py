
# Question 1: How do you convert a string to lowercase?


greeting = "Hello World"
print(greeting.lower())  # Answer: 'hello world'

# Question 2: How do you convert a string to uppercase?
greeting = "Hello World"
print(greeting.upper())  # Answer: 'HELLO WORLD'

# Question 3: How do you capitalize the first letter of a string?
sentence = "hello world"
print(sentence.capitalize())  # Answer: 'Hello world'

# Question 4: How do you capitalize the first letter of every word in a string?
sentence = "hello world"
print(sentence.title())  # Answer: 'Hello World'

# Question 5: How do you swap the case of letters in a string?
greeting = "Hello World"
print(greeting.swapcase())  # Answer: 'hELLO wORLD'
# 
# 2. String Stripping
# Question 6: How do you remove leading and trailing spaces in a string?
padded_text = "  Hello World  "
print(padded_text.strip())  # Answer: 'Hello World'
# Question 7: How do you remove only the leading spaces in a string?
padded_text = "  Hello World  "
print(padded_text.lstrip())  # Answer: 'Hello World  '

# Question 8: How do you remove only the trailing spaces in a string?
padded_text = "  Hello World  "
print(padded_text.rstrip())  # Answer: '  Hello World'
# 3. Searching and Finding
# Question 9: How do you find the index of the first occurrence of a substring?
programming_sentence = "Python programming is fun"
print(programming_sentence.find('prog'))  # Answer: 7
# Question 10: How do you find the index of the last occurrence of a substring?

programming_sentence = "Python programming is fun"
print(programming_sentence.rfind('o'))  # Answer: 16

# Question 11: How do you check if a substring is in a string and get its index?
programming_sentence = "Python programming is fun"
print(programming_sentence.index('fun'))  # Answer: 20

# Question 12: How do you count the number of occurrences of a character in a string?
programming_sentence = "Python programming is fun"
print(programming_sentence.count('o'))  # Answer: 3

# 4. Checking String Content
# Question 13: How do you check if a string contains only letters?
alphanumeric_string = "Python123"
print(alphanumeric_string.isalpha())  # Answer: False

# Question 14: How do you check if a string contains only digits?
numeric_string = "12345"
print(numeric_string.isdigit())  # Answer: True

# Question 15: How do you check if a string contains only alphanumeric characters?
alphanumeric_string = "Python123"
print(alphanumeric_string.isalnum())  # Answer: True

# Question 16: How do you check if a string is in lowercase?
lowercase_string = "python"
print(lowercase_string.islower())  # Answer: True

# Question 17: How do you check if a string contains only spaces?
whitespace_string = "   "
print(whitespace_string.isspace())  # Answer: True
# 5. Joining and Splitting Strings

# Question 18: How do you join a list of strings with a space?
words_list = ['Python', 'is', 'fun']
print(' '.join(words_list))  # Answer: 'Python is fun'

# Question 19: How do you split a string into a list of words?
phrase = "Python is fun"
print(phrase.split())  # Answer: ['Python', 'is', 'fun']

# Question 20: How do you split a string by a specific delimiter?
hyphenated_string = "Python-is-fun"
print(hyphenated_string.split('-'))  # Answer: ['Python', 'is', 'fun']

# 6. Replace and Format
# Question 21: How do you replace a substring with another substring?
sentence = "I love programming"
print(sentence.replace("programming", "Python"))  # Answer: 'I love Python'

# Question 22: How do you format a string with placeholders?
user_name = "Divansh"
user_age = 20
print("My name is {} and I am {} years old.".format(user_name, user_age))
# Answer: 'My name is Divansh and I am 20 years old.'

# Question 23: How do you use f-strings for formatting?
user_name = "Divansh"
user_age = 20
print(f"My name is {user_name} and I am {user_age} years old.")
# Answer: 'My name is Divansh and I am 20 years old.'

# 7. Encoding and Decoding
# Question 24: How do you encode a string to bytes?
plain_text = "Hello"
print(plain_text.encode('utf-8'))  # Answer: b'Hello'
# Question 25: How do you decode bytes back to a string?
encoded_text = b'Hello'
print(encoded_text.decode('utf-8'))  # Answer: 'Hello'

# 8. String Alignment
# Question 26: How do you center-align a string with a specific character?
programming_language = "Python"
print(programming_language.center(20, '-'))
# Answer: '-------Python-------'

# Question 27: How do you left-align a string with a specific character?
programming_language = "Python"
print(programming_language.ljust(20, '-'))
# Answer: 'Python-------------'

# Question 28: How do you right-align a string with a specific character?
programming_language = "Python"
print(programming_language.rjust(20, '-'))
# Answer: '-------------Python'

# 9. Miscellaneous
# Question 29: How do you check if a string starts with a specific substring?
sentence = "Python is fun"
print(sentence.startswith("Python"))  # Answer: True

# Question 30: How do you check if a string ends with a specific substring?
sentence = "Python is fun"
print(sentence.endswith("fun"))  # Answer: True

# Question 31: How do you pad a string with zeros?
number_string = "42"
print(number_string.zfill(5))  # Answer: '00042'

# Question 32: How do you split a string into lines?
multiline_string = "Hello\nWorld\nPython"
print(multiline_string.splitlines())
# Answer: ['Hello', 'World', 'Python']

text = "Hello, how are you?"
words = text.split(",")
print(words)
