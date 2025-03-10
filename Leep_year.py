year = int(input("Enter Your Number: "))
if year % 400 == 0 :
   if year % 100 == 0 :
        print("This a Leep Year")
   else:
        print("This Not Leep Year")
else:
   if year % 4 == 0:
       print("This Leep Year")
else:
print("This Not Leep Year")
