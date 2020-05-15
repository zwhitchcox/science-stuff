import sys

# program to count password possibilities

n = int(input("Enter number of characters allowed in password (e.g. A-Z, a-z, 0-9 = 62): "))
k = int(input("Enter length of password: "))

print(f'The number of possible characters is {n**k:,}.')