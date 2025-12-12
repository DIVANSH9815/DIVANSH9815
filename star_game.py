'''
   *
  ***
 *****

'''


number = int(input("enter a number:"))
for i in range(1,number+1):
    print(" "*(number-i),end="")
    print("*"*(2*i-1),end="")
    print()
    

'''
  *
  *
  ***

'''

value= int(input("enter a number:"))
for i in range(1,value+1):
    print("*"*i,end="")
    print()



'''
 *****
 *   *
 *****

'''

num = int(input("enter a number: "))
for i in range(1,num+1):
    if(i==1 or i==num):
        print("*"*num,end="")
    else:
        print("*",end="")
        print(" "*(num-2),end="")
        print("*",end="")
    print("")
