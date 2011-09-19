"""
How many n-digit positive integers exist which are also an nth power?
"""

# easy to calculate, but I'm not sure what the upper bound is so this will
# just run until it's interrupted.
# clearly though, the exponential will grow a lot faster than the number of
# digits so I guess you could come up with some way of figuring out the
# upper bound

from lib import euler

integers = []
for power in euler.integers(1):
  for base in euler.integers(1):
    x = base**power
    if len(str(x)) == power:
      integers += [x]
      print len(list(set(integers)))
    elif len(str(x)) > power: break
