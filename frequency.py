s=input("Enter a string")
ns=""
for i in s:
    if i not in ns:
        ns=ns+i
#print(ns)
for j in ns:
    c=0
    for k in s:
        if(j==k):
            c=c+1
    print(f"frequency of {j} is {c}")               