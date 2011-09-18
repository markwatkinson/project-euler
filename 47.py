 
"""
Find the first four consecutive integers to have four distinct primes factors.
What is the first of these numbers?
"""

"""

General plan is to iterate over the integers, generate a list of primes as
we go, up to n/2, then see how many of those primes divide n.

It's a bit slow, about 1 minute 20 here. Can't see how to optimise it though,
except for pre-generating primes

"""

from lib import euler
import math
prime_generator = euler.primes()
primes = [prime_generator.next()]
i = 1
num = 4
factors = [0]

while i:
  found = True
  while primes[-1] < i/2:
    p = prime_generator.next()
    primes += [p]

  num_factors = 0
  for p in primes:
    if i % p == 0:
      num_factors += 1
      if num_factors >= num: break
    
  factors += [num_factors]
  if min(factors[-num:]) >= num:
    print i-num + 1
    break
  i += 1