import math

numBooks = int(input("Input number of books, and I will tell you how many ways to organize them there are: "))
print(f'There are {math.factorial(numBooks)} ways to organize {numBooks} books.')