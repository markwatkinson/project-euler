 
"""
http://projecteuler.net/index.php?section=problems&id=44
"""

import math
from sys import exit
from lib import euler

def pentagonal_number():
  n = 1
  while 1:
    yield n*(3*n-1)/2
    n+=1


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
    if euler.is_pentagonal(p1 + p2):
      diff1 = p2-p1
      diff2 = p1-p2
      if (euler.is_pentagonal(diff1)) or (euler.is_pentagonal(diff2)):
        print abs(p1-p2)
        exit()
  
  pentagonals += [p1]