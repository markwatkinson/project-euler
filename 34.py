"""
Find the sum of all numbers which are equal to the sum of the factorial of
their digits.
"""


import math

# I don't know exactly where the upper bound is, but it should be pretty low
# After all, 9! is massive so any number with a 9 in it is pretty unlikely.
# Let's guess at 1m

answers = []
for x in range(10, 10**6):
  factorials = [math.factorial(int(n)) for n in str(x)]  
  s = sum(factorials)
  if s == x:
    answers += [x]

print sum(answers)