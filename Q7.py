#python program to input 10 numbers and sort them into two lists odd and even respectively

l,o,e=[],[],[]
print("Enter 10 numbers")
for i in range(0,10):
    a=int(input())
    l.append(a)
for i in l:
    if(i%2==0):
        e.append(i)
    else:
        o.append(i)
print("Even numbers list: \n",e)        
print("Odd numbers list: \n",o)