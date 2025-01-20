operator = input("Enter your operator like(-,+,/,*): ")
num1 = float(input("enter your 1st number: "))
num2 = float(input("enter your 2nd number: "))


if operator == "+":
    result = num1 + num2
    print(round(result,3))
elif operator == "-":
    result = num1 - num2
    print(round(result,3))
elif operator == "*":
    result = num1 * num2
    print(round(result,3))
elif operator == "-":
    result = num1 / num2
    print(round(result,3))
else:
    print("noting gonna be wrong plase check it!")