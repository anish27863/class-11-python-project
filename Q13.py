#Random number generator

import random
a=int(input("enter starting number of the range\n"))
b=int(input("enter ending number of the range\n"))

x=random.randint(a,b)
print(f"Random number generated in the range ({a},{b}) is {x}")