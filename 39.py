
"""
if {a,b,c} is a Pythagorean triplet and a+b+c = p,
For which value of p <= 1000, is the number of solutions maximised?
"""

"""
we showed in problem 9 that

a + b + sqrt(a*a + b*b) = p

which neatly gets rid of the third variable.

given that we know a+b < p, and p <= 1000, we can brute force this pretty
quickly.
"""


import math
solns = [[]]*1001



# this grid is going to be a lookup table of (a, b) => a + b + sqrt(a*a + b*b)

grid = []
for a in range(1000):
  row = []
  for b in range(1000):
    p = a + b + math.sqrt(a*a + b*b)
    row += [p if int(p) == p and p <= 1000 else None]
  grid += [row]

# now all we have to do is figure out which element is the most popular, and
# that's our p

# note that this isn't technically consistent with the question - we have
# duplicates in ours, i.e. swap a and b's values.
# But we still have enough information to figure out which is the most
# popular, which is what the question asks.
counts = {}
for row in grid:
  for element in row:
    counts[element] = counts.get(element, 0) + 1

counts_ = counts.items()
counts_ = filter(lambda x: x[0] is not None, counts_)
counts_.sort(lambda a, b: a[1]-b[1])
print 'p =', int(counts_[-1][0])
