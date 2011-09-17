 
"""
http://projecteuler.net/index.php?section=problems&id=44
"""

import math
from sys import exit


def pentagonal_number():
  n = 1
  while 1:
    yield n*(3*n-1)/2
    n+=1

def is_pentagonal(number):
  # p = n(3n-1)/2
  # we need to see if there exists a real integer solution for n given that we
  # know p
  # 2p = n(3n-1)
  # 2p = 3n**2 - n
  # 3n**2 - n - 2p = 0
  # quadratic in n
  # n = (1 +- sqrt(1 - 4*3*(-2p)))/2*3
  # n = (1 +- sqrt(1 + 24p))/6
  
  determinant = math.sqrt(1 + 24*number)
  n = ( (1 + determinant)/6, (1 - determinant)/6)
  for soln in n:
    if soln >= 1 and int(soln) == soln: return True
  return False


"""
We are looking for the closest pair of pentagonals whose sum and difference
is pentagonal, and for which the difference is minimise.

As the intervals in the pentagonal sequence appear to get bigger continually,
we can iterate backwards and take the first one we find? That will have
the minimised difference
"""


pentagonals = []
for p1 in pentagonal_number():
  for p2 in pentagonals[::-1]:
    if is_pentagonal(p1 + p2):
      # these can be either way around but we need to care about negatives
      # or my quadratic solver borks
      # they wouldn't be a valid solution anyway.
      diff1 = p2-p1
      diff2 = p1-p2
      if (diff1 > 1 and is_pentagonal(diff1)) or (diff2 > 1 and is_pentagonal(diff2)):
        print abs(p1-p2)
        exit()
  
  pentagonals += [p1]