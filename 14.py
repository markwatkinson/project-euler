#!/usr/bin/env python

"""
n -> n/2 (n is even)
n -> 3n + 1 (n is odd)
find the longest chain for starting n < 1m

it is important to note that we can cache a lot of the results here
"""

chains = {}
chains[1] = 1

def chain_step(n):
  if n%2: return 3*n + 1
  else: return n/2

def chain(n):
  if chains.get(n, 0) != 0: return chains[n]
  else:
    # some neat recursion
    steps = 1 + chain(chain_step(n))
    chains[n] = steps
    return steps

max_data = (0, 0)
for n in xrange(1, 10**6):
  steps = chain(n)
  if steps > max_data[1]:
    max_data = (n, steps)

print 'starting number, steps =', max_data