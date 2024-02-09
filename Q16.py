#Compound interest calculator

r=float(input("Enter principal amount: "))
p=float(input("Enter rate of interest: "))
t=float(input("Enter time in years: "))

a=p*(1+r/100)**t
ci=a-p

print(f"Amount after {t} years = {a}")
print(f"Interest earned= {ci}")