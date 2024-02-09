import math
a=int(input("Enter a number"))
sp=a
for i in range(0,a):
    for j in range(sp,0,-1):
        print(" ",end="")
    sp-=1
    #val=0
    for k in range(0,i+1):
        z=i-k
        #val=math.factorial(i)/(math.factorial(k))*(math.factorial(z))
        val=math.comb(i,k)
        val=int(val)
        print(val,end=" ")
    print()       