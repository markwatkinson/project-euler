
"""
Find the sum of all products whose multiplicand/multiplier/product
identity can be written as a 1 through 9 pandigital.
"""

# brute force?

import math

def is_pandigital(n):
  # checks for 1-9 pandigital
  s = str(n)
  if len(s) > 9: return False # duplicates
  for x in range(1, 10):
    if not str(x) in s: return False
  return True


answers = []

# a*b needs to be 9 digits long, so we only need to check up to the square root
# of 999999999. 
limit = int(math.sqrt(999999999))

for a in xrange(1, limit):
  for b in xrange(1,limit):
    n = str(a) + str(b) + str(a*b)
    if len(n) > 9: break
    if len(n) < 9: continue
    if is_pandigital(n): answers += [a*b]

print sum(list(set(answers)))
    