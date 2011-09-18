 
"""
How many, not necessarily distinct, values of  nCr, for 1 <= n <= 100, are
greater than one-million?

"""
import math

from lib import euler

# as we all know, the combination function is pascal's triangle, which
# is symmetrical, so we only need to check half of it, but there are so
# few values to check that it hardly seems worth worrying about

num = 0

# we've already been told not to look below n=23 in the question
for n in range(23, 101):
  for r in range(2, n):
    if euler.combination(n, r) > 10**6:
      num += 1

print num