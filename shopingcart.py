foods = []
prices = []
total = 0

while True:
    food = input("Enter your food as your like(Q to quit): ")
    if food == "q":
        break 
    else:
        price = float(input("Enter a curent price for food: "))
    foods.append(food)
    prices.append(price)

result = "--- YOUR CART ---"
final_name = result.center(32,"-")
print(final_name)
for food in foods:
    print(food,end=" ")
for price in prices:
    total += price
print()
print(f"Your total amount is: {total}")
result = "---Thankks visting next time ---"
final_result= result.center(32,"-")
print(final_result)
