 
"""
Find the smallest prime which, by replacing part of the number (not necessarily
adjacent digits) with the same digit, is part of an eight prime value family.
"""

"""
this question is kind of confusing. 
"""

import sys
from lib import euler

primes = []
primes_map = {}
with open('data/primes') as f:
  primes = [int(n) for n in f.read().splitlines()]
for p in primes:
  primes_map[p] = True
print 'got primes'

# Let's try replacing two digits first

for p in primes:
  if p < 100: continue
  s = str(p)

  # educated guess: the first to 7 primes requires two replacement positions
  # if we want 8, let's go for three. It'll be faster than trying loads.
  for i in range(len(s)):
    for j in range(i+1, len(s)):
      for k in range(j+1, len(s)):

        primes_ = {}
        # now we iterate over each possible replacement
        for r in range(10):
          replaced_ = list(s)
          replaced_[i] = str(r)
          replaced_[j] = str(r)
          replaced_[k] = str(r)
          replaced = int(''.join(replaced_))
          if len(str(replaced)) < len(s): continue
          if replaced in primes_map:
            primes_[replaced] = True
            if len(primes_) >= 8:
              print primes_
              print min(primes_.keys())
              sys.exit()
              