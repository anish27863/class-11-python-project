#Simple calculator

print("-----MENU-----")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
c=int(input("Enter your choice"))
a=float(input("Enter first number"))
b=float(input("Enter second number"))

if(c==1):
    print("Sum= ",a+b)
elif(c==2):
    print("Difference= ",a-b)
elif(c==3):
    print("Product= ",a*b)
elif(c==4):
    print("Quotient= ",a/b)
else:
    print("Error")
