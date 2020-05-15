import sys
import math

numChars = int(input("Enter number of characters allowed in password (e.g. A-Z, a-z, 0-9 = 62): "))
passLen = int(input("Enter length of password: "))

print(f'The number of possible characters with no repeating characters is {int(math.factorial(numChars)/math.factorial(numChars - passLen)):,}.')