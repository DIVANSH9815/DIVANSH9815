
# text1 = "stra$e"
# # text2 = "strake"
# # print(text1.casefold() == text2.casefold())

# text = "Python is great i am fan  this languafge & ***"
# result = text.encode("ascii", errors ="replace")
# print(result)  # Output: b'Python'


# text = "python \t is best me ever language"
# # result = text.expandtabs(23)
# # print(result)

# data = {"name":"Divanh","age":21 }
# text = "i am {name}and i am {age}years old "
# result = text.format_map(data)
# print(result)

# text = "python@"
# print(text.isascii())

# text = "Divansh Sharma"
# print(text.istitle())

# text = "Divansh sharma"
# print(text.istitle())


# text = "divansh Sharma"
# print(text.istitle())

# txt = "Hello Sam!"
# mytable = str.maketrans("Hello", "Pytho")
# print(txt.translate(mytable))  

# age = int(input("Enter a Your Age: "))

# while age<0:
#     print("Age cant be negetive")
#     age = int(input("Enter a Your Age: "))
# # print(f"your age is {age} year old ")


# num = int(input("Enter a number: "))

# while num < 0 or num > 10:
#     print(f"This number is not valid{num}")
#     num = int(input("Enter a number: "))
# print(f"this a correct {num} num")


# count = 0
# while count < 5:
# #     print(f"Count is:{count}")
# #     count += 1

# count = 0
# while count < 5:
#     count += 1
#     if count == 3:
#         continue  # Skip the iteration when count is 3
#     print("Count is:", count)

time_left = 10
while time_left > 0:
    print("Time left:", time_left)
    time_left -= 1
print("Time's up!")
