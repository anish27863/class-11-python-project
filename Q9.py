#python program to convert a decimal number to binary
a=int(input("Enter a number"))
s=""
while(a!=0):
    if(a%2==0):
        s=s+"0"
    else:
        s=s+"1"
    a=a//2
print(s[ : :-1])        