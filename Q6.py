#python program to calculate grade of a student based on average of 5 sub marks
a=int(input("Enter marks obtained in Physics "))
b=int(input("Enter marks obtained in Chemistry "))
c=int(input("Enter marks obtained in Maths "))
d=int(input("Ener marks obtained in Computer Science "))
e=int(input("Enter marks obtained in English "))
s=a+b+c+d+e
avg=s/5
if(avg>=90 and avg<=100):
    g='a'
elif(avg>=70 and avg<90):
    g="b"
elif(avg>=50 and avg<70):
    g="c"
elif(avg>=40 and avg<50):
    g="d"
elif(avg<40):
    g="fail"
else:
    print("Invalid input")
    exit()
    
print("Total marks= ", s)
print("Average= ",avg)                   
print("Grade= ", g)