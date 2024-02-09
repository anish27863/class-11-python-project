#python program to find the factorial of a number

num=int(input("Enter a number\n"))
f=1

if(num<0):
    print("Factorial does not exist for negative numbers")
else:
    for i in range(1,num+1):
        f=f*i
    print(f"The factorial of {num} is {f} ")    