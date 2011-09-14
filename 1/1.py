#!/usr/bin/env python

from math import ceil

# find the sum of all multiples of 3 and 5 below 1000

limit = 1000

multiples = []

for x in [3, 5]:
  multiples += [x*i for i in range(1, int( ceil(limit/float(x)) ) )]

# uniquify the list
multiples = list(set(multiples))
print multiples
print sum(multiples)