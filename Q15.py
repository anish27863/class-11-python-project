#Python program to remove all duplicates from a string

s=input("Enter a number\n")
p=""

for char in s:
    if char not in p:
        p=p+char

print(f"The string after removing all the duplicates is {p}")        