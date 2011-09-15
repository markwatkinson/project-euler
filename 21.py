
"""Evaluate the sum of all the amicable numbers under 10000."""

from lib import euler

d = lambda x: sum(euler.divisors(x)[:-1])

amicables = []
for a in xrange(1, 10000):
  b = d(a)
  if b != a and d(b) == a: amicables += [a, b]

# might be some duplication
print sum(list(set(amicables)))
