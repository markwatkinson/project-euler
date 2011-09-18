"""
Which prime, below one-million, can be written as the sum of the most
consecutive primes?
"""

# seems easy: generate list of primes up to 1m and have a look

from lib import euler


generator = euler.primes()
primes = [] # list of primes, as an optimisation, this only goes up to
#the last two primes p1 and p2 where p1 + p2 < 1m
primes_map = {} # lookup, this goes up to 1m
last_p = 0
for p in euler.primes():
  if p > 10**6: break
  if p + last_p < 10**6:
    primes += [p]
  last_p = p
    
  primes_map[p] = True

print 'generated primes', len(primes)

max_ = (0, 0)



for i, p in enumerate(primes):
  #print p
  sum_ = p
  for j, px in enumerate(primes[i+1:]):
    sum_ += px
    if sum_ > 10**6: break
    if j+2 > max_[1] and sum_ in primes_map:
      max_ = (sum_, j+2)
print max_
