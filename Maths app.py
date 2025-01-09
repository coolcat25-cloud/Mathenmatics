print("Hello User!")
print("Welcome to the Maths App!")
print("Please select the type of mathematical calculation you want to be done  from the choices below")
#The choices
print("#Addition = 1        #Square roots = 5")
print("#Substraction = 2    #Cube numbers = 6")
print("#Multiplycation = 3")
print("#Division = 4")
import math

choice = int(input("Enter the number of your choice:"))
if choice == 1:
    print("You have chosen Addition!")
    print("Enter the number you want to add onto the spaces below")
    print("If there is no third number,enter '0' on the third entry")
    a = float(input("Enter the first number:"))
    b = float(input("Enter the second number:"))
    c = float(input("Enter the third number:"))
    if c == "-":
          ans = a+b
          print(a,"+",b,"=",ans)
    else:
        ans = a+b+c
        print(int(a,"+",b,"+",c,"=",ans))
if choice == 2:
    print("You have chosen Substraction!")
    print("Enter the number you want to substract onto the spaces below")
    print("If there is no third number,enter '0' on the third entry")
    a = float(input("Enter the first number:"))
    b = float(input("Enter the second number:"))
    c = float(input("Enter the third number:"))
    if c == "-":
          ans = a-b
          print(a,"-",b,"=",ans)
    else:
        ans = a-b-c
        print(a,"-",b,"-",c,"=",ans)
if choice == 3:
    print("You have chosen Multiplication!")
    print("Enter the number you want to multiply onto the spaces below")
    a = float(input("Enter the first number:"))
    b = float(input("Enter the second number:"))
    ans = a*b
    print(a,"*",b,"=",ans)
if choice == 4:
    print("You have chosen Division!")
    print("Enter the number you want to divide onto the spaces below")
    a = float(input("Enter the first number:"))
    b = float(input("Enter the second number:"))
    ans = a/b
    print(a,"/",b,"=",ans)
if choice == 5:
    print("You have chosen square rooting!")
    a = float(input("Enter the number:"))
    ans = a**0.5
    print("The square root of",a,"is",ans)
if choice == 6:
    print("You have chosen to try cubing!")
    a = float(input("Enter the number you want cubed:"))
    ans = a*a*a
    print("When you cube",a,",you get the value",ans)
input("Press Enter to exit...")
    
