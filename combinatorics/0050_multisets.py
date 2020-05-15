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
#
# for reference matrix: https://imgur.com/a/xBfITSQ

print("This program will tell you how many possible donut orders there are.")
n = int(input("Enter the total number of donut choices: "))
k = int(input("How many donuts in an order? (e.g. 12) "))
multisets = math.factorial(k + n - 1) / (math.factorial(k) * math.factorial(n - 1))
print(f'There are {int(multisets):,} possible donut orders of size {k}.')