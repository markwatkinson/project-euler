#!/usr/bin/env python


"""By considering the terms in the Fibonacci sequence whose values do not
exceed four million, find the sum of the even-valued terms."""


fibonacci = [1, 2]

# build fibonacci sequence, store entirely in memory
while fibonacci[-1] <= 4*10**6:
  fibonacci += [sum(fibonacci[-2:])]
print fibonacci
print sum( filter(lambda f: not f%2, fibonacci) )
