menu ={
	   "pizza" : 5.34,
       "bugger":3.34,
       "cofee" :6.45,
       "pokcorn":7.56,
       "momos" : 5.45,
       "maggi" : 3.45
      }

cart =[]
total=0


print("--------MENU-------")
for key,value in menu.items():
    print(f"{key:10} {value:.2f}")

while True:  
    food =input("enter yor food as you like(Q to quit)").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)
print("------ YOUR ORDER -------")
for food in cart:   
    total+=menu.get(food)
    print(food,end=" ")
print()
print(f"your total is ${total}")   
