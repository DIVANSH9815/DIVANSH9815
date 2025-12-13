def calculate_bill(amount,tax=5):
    final_amount = amount+(amount * tax / 100)
    return final_amount

amount = int(input("Enter a Number: "))

choice= input("enter a tax percentage(yes/no): ")

if choice.lower() =="yes":
    tax = int(input("enter a tax value: "))
    result_value = calculate_bill(amount,tax)

else:
    result_value =calculate_bill(amount)

print(f"thanks for visiting {result_value}")
