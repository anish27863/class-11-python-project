n=int(input("Enter no of terms to enter"))
l,e,o,f=[],[],[],[]
x,a=0,0
for i in range(0,n):
    l=int(input("Enter a number"))
for j in range(0,n):
    if(j%2==0):
        e.append(l[j])
    else:
        o.append(l[j])
        
for k in range(0,n):
    if(n%2==0):
        f.append(o[x])
    else:
        f.append(0)
    x+=1
print(f)            
               