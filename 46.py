 
"""
What is the smallest odd composite that cannot be written as the sum of a prime
and twice a square?
"""

from lib import euler

from sys import exit

"""
What we're going to do here is iterate over odd integers indefinitely,
filling up an array of primes and squares up to the current integer as we go.
Then we're going to iterate over the primes, subtracting the prime from the
integer, and seeing if the difference can be made up in the list of squares

HURRAH FOR GENERATORS
"""

def squares():
  for x in euler.integers(1):
    yield x**2

prime_generator = euler.primes()
square_generator = squares()

"""Using dicts for speedy lookup"""
primes = {}
squares = {}
for i in euler.integers(9, 2):
  
  while 1:
    p = prime_generator.next()
    primes[p] = True
    if p > i: break
  while 1:
    s = square_generator.next()
    squares[s] = True
    if s > i: break
  if i in primes: continue
  found = False
  for p in primes.keys():
    diff = i - p
    if diff > 0:
      diff/=2
      if int(diff) == diff:
        diff = int(diff)
        if diff in squares:
          found = True
          break
  if not found:
    print i
    break