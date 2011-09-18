
from lib import euler

import sys

"""
Find a set of 5 primes for which any two members concatenated also produces
a prime
"""


# this is hard.
# this runs in about 5 minutes, so it's clearly not the best solution
# What we do is generate a growing list of primes, then iterate over it to find
# each combination of five numbers, and test them.
# the 5 nested for loops could be neater written recursively but I don't
# imagine that will help the runtime

primes = []
primes_map = {}


def concat(a, b):
  return int(str(a) + str(b))

def are_prime(l):
  for n in l:
    is_p = primes_map.get(n, None)
    if is_p is None:
      is_p = euler.is_prime(n)
      primes_map[n] = is_p
    if not is_p: return False
  return True


for i, p1 in enumerate(euler.primes()):
  #print p1
  primes += [p1]
  primes_map[p1] = True

  for j, p2 in enumerate(primes):
    c = [concat(p1, p2),
        concat(p2, p1)]
    if not are_prime(c): continue
    for k, p3 in enumerate(primes[j+1:]):
      c = [
        concat(p1, p3),
        concat(p3, p1),
        concat(p2, p3),
        concat(p3, p2),
      ]
      if not are_prime(c): continue
      for l, p4 in enumerate(primes[j+k+1:]):
        c = [
          concat(p1, p4),
          concat(p4, p1),
          concat(p2, p4),
          concat(p4, p2),
          concat(p3, p4),
          concat(p4, p3)
        ]
        if not are_prime(c): continue

        for m, p5 in enumerate(primes[j+k+l+1:]):
          c = [
            concat(p1, p5),
            concat(p5, p1),
            concat(p2, p5),
            concat(p5, p2),
            concat(p3, p5),
            concat(p5, p3),
            concat(p4, p5),
            concat(p5, p4)
          ]
          if not are_prime(c): continue

          print p1, p2, p3, p4, p5
          print sum([p1, p2, p3, p4, p5])
          sys.exit()
