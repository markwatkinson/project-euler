 
"""
http://projecteuler.net/index.php?section=problems&id=58
"""

from lib import spiraldiagonals
from lib import euler

"""
this is pretty easy - we can generate the diagonals indefinitely from the
formula we came up with in q28 and simply check the prime ratio

it's a bit slow, probably the prime check, but still less than a minute
"""

primes = []
ds = [1]
for i, diagonals in enumerate(spiraldiagonals.diagonals()):
  
  for d in diagonals:
    ds += [d]
    if euler.is_prime(d): primes += [d]
  ratio = float(len(primes)) / len(ds)
  if ratio <= 0.1:
    print (i+1)*2 + 1  # this is the spiral width
    break
    