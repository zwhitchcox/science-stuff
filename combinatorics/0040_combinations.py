import math

# If we want to find k-permutations of an n-set, and order doesn't matter, we basically do the same thing as before
# (n!/(n - k)!), only now, because we don't care about the order, we need to divide by the total number of permutations
# of k (or k!), so the new formula is
#
# n! / (n - k)! / k!
#
# or
# 
# n!/ [k!(n - k)!]
#
# which is called "n choose k".
# 
# The word "combination" is sometimes used indicate an unordered collection of distinct objects.
# You could also characterize this as the number of k-element subsets in an n-element set

n = 52
k = int(input("Enter number of cards in a hand, and I will tell you how many possible hands there are: "))
combinations = math.factorial(n) / math.factorial(n - k) / math.factorial(k)
print(f'There are {int(numHands):,} possible combinations for a {cardsInHand}-card hand.')