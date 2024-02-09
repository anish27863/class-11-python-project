n=int(input("Enter no of terms to enter"))
l,e,o,f=[],[],[],[]
for i in range(0,n):
    p=0
    p=int(input("Enter a number"))
    l.append(p)
   
for j in range(0,n):
    if(j%2==0):
        e.append(l[j])
    else:
        o.append(l[j])
print(e,"\n" ,o)
a=0       
for k in range(0,n):
    f.append(o[a])
    f.append(e[a])
    #x=x+1
    if(n<len(e)):
        a=a+1

for y in range(0,2):
    print(l[y])           
               