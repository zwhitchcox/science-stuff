import sys
import math

# this is called a "k-permutation", where k is the number of permutations we take
# here, the password length is the number of permutations
# the formula is

#   n!/(n - k)!

# where in is the size of the set (which would here be number of characters allowed in the password),
# and k is the size of the permutation (here, the length of the password)

n = int(input("Enter number of characters allowed in password (e.g. A-Z, a-z, 0-9 = 62): "))
k = int(input("Enter length of password: "))

kPermutations = math.factorial(n)/math.factorial(n - k)

print(f'The number of possible characters with no repeating characters is {kPermutations:,}.')