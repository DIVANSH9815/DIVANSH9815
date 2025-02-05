def balance_show():
  print("**************************")
  input(f"YOur Amount Is ${balance:.2f}: ")
  print("**************************")
  
def deposit():
  print("**************************")
  amount = float(input("Enter your Amount as a doposit: "))
   
  if amount < 0:
    print("Thats Not Valid Amount")
    return 0
  else:
    return amount
  print("**************************")
  
def withraw():
  print("**************************")
  amount =float(input("Enter Your Amount as an withraw cash: "))
   
  if amount > balance:   
   print("Insuffisent Balnce check plz")
  elif amount < 0:
    print("number must be greater than 0")
    return 0
  else:
      return amount 
balance = 0
is_running = True

while is_running:
  
    print("**************************")
    print("Wellcome To our SBI bank")
    print("1. Check")
    print("2. doposit")
    print("3. withraw")
    print("4. Exit")
    print("**************************")
    
    
    choice = input("Enter yor choice (1 - 4): ")
    
    if choice == "1":
      balance_show()
      
    elif choice == "2":
      balance += deposit()
      
    elif choice == "3":
      balance -= withraw()
      
    elif choice == "4":
      is_running = False
      
    else:
      print("**************************")
      print("That Number Is Not Valid ")
      print("**************************")
print("**************************")
print("Thanks For Visiting Our Bank")
print("**************************")
