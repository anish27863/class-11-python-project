#Python program to generate the fibonacci series

n=int(input("Enter number of terms you wish to generate\n"))
n1,n2,c=0,1,0

if(n<=0):
    print("please enter positive numbers")

elif(n==1):
    print(n1)

else:
    print("The series is: ")
    while(c<n):
        print(n1)
        nth=n1+n2
        n1=n2
        n2=nth
        c+=1