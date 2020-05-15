import math

# a permutation is a list with no repeating characters
# here we see the number of permutations you can order a set of books in.
# For instance, if you have 8 books, there are 8! possible permutations.
# Since we're using every single book, this is called a "complete permutation"

n = int(input("Input number of books, and I will tell you how many ways to organize them there are: "))
print(f'There are {math.factorial(n)} ways to organize {n} books.')