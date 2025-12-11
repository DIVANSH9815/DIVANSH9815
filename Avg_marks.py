marks_1 = int(input("Enter 1st Number: "))
marks_2 = int(input("Enter 2nd Number: "))
marks_3 = int(input("Enter 3rd Number: "))
marks_4 = int(input("Enter 4th Number: "))
marks_5 = int(input("Enter 5th Number: "))
marks_6 = int(input("Enter 6th Number: "))
marks_7 = int(input("Enter 7th Number: "))
marks_8 = int(input("Enter 8th Number: "))
marks_9 = int(input("Enter 9th Number: "))

Total_percentage = (100 * (marks_1 + marks_2 + marks_3 + marks_4 + marks_5 + marks_6 + marks_7 + marks_8 + marks_9)) / 900

if Total_percentage >= 40:
    print(f"Passed : {Total_percentage}")

elif 33 <= Total_percentage < 40:
    print(f"Passed but low percentage: {Total_percentage}")

else:
    print(f"Failed! Try next time: {Total_percentage}")
