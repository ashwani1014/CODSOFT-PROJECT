print('Hii I am calculator 🤗')


Num1=float(input('enter the number Num1 : '))
Num2=float(input('enter the number Num2 : '))
 
print("Press 1 for addition ")
print("Press 2 for subtraction ")
print("Press 3 for multiplication")
print("Press 4 for Division ")
print("Press 5 for remindar ")


choice=int(input("Enter your choice as per your need  "))


if choice==1:
    print(Num1+Num2) 
    
elif choice==2:
    print(Num1-Num2)
 
elif choice==3:
    print(Num1*Num2)
    
elif choice==4:
    print(Num1/Num2)

elif choice==5:
    print(Num1%Num2)
 
else:
    print('Not correct choice')

print("   Thank You  ")