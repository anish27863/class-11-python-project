#python program to enter a string and display each letter in it along with its ascii code\

a=input("Enter a string\n")
print("LETTER       ASCII CODE")
for i in a:
    print(i,"           ",ord(i))
