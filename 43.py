 
"""
0-9 pandigitals with substring divisibility properties.
http://projecteuler.net/index.php?section=problems&id=43
"""

# there are 10! 0-9 pandigital numbers. This isn't *too* bad, we can brute
# force them.


# this is a bit slow, I guess my inefficient string based permutation function
# is slowing things down. It's still less than a minute though.


# we could make optimisations based on the the triplet sequences, we know the
# last three digits have to be divisible by 17, which greatly reduces the
# search space for the other digits.
# but that requires writing a more intelligent permutation function

from lib import euler

digits = '0123456789'

divisors = [0, # we never check this, obviously
            2, 3, 5, 7, 11, 13, 17]
numbers = []


for permutation in euler.permutate(digits):
  skip = False
  # fewer numbers will be divisible by 17 than 2, so let's work backwards
  # for speed
  for x in xrange(7, 0, -1):
    if int(permutation[x:x+3]) % divisors[x] != 0:
      skip = True
      break
  if skip: continue
  numbers += [int(permutation)]
  print 'found {0}'.format(permutation)

print 'sum =', sum(numbers)