#python program to input names of employees and salaries and store them in a dictionary
n=int(input("Enter the number of employees whose data is to entered"))
employee=dict()
while(n!=0):
    nm=input("Enter name of employee ")
    sl=int(input("Enter salary "))
    employee[nm]=sl
    n-=1
print("Employee name\t\tsalary")
for k in employee:
    print(k,"\t\t",employee[k])    