import math

# in a "multiset", order doesn't matter, (like a set, but unlike a list), but repetition is allowed
# (like a set, but unlike a list)
#
# The formula for a multiset is "(k + n - 1) choose k" or
#
# (k + n - 1)! / (k!(n - 1)!)
#
# this is because we are basically adding the total number of choices we have already picked
# back into the pool of available choices, because duplicates do not matter. But everything else is
# the same from "combinations". Also, we subtract 1, because there is no danger of repetition on the 
# first choice.

n = int(input("Enter the total number of donut choices, and I'll tell you how many possible orders there are: "))
k = int(input("How many donuts in an order? "))
multisets = math.factorial(k + n - 1) / (math.factorial(k) * math.factorial(n - 1)
print(f'There are {multisets} possible donut orders of size {k}.')