print("quadratic Equation solver")
a=int(input("Enter the value of a "))
b=int(input("Enter the value of b "))
c=int(input("Enter the value of c "))
x1=(-b+(b*b-4*a*c)**0.5)/2*a
x2=(-b-(b*b-4*a*c)**0.5)/2*a
print("The roots are: ")
print(x1)
print(x2)