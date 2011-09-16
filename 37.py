
"""
Find the sum of the only eleven primes that are both truncatable from
left to right and right to left.

"""

# we don't know the upper bound, but since there's only 11 of them we don't
# need to, I guess.

from lib import euler

truncatable = []
primes = {} # we'll want to look up numbers we've already generated for primality
for p in euler.primes():
  primes[p] = True
  if p < 10: continue

  # truncate
  p_ltr = str(p)
  p_rtl = str(p)
  t = True
  while p_ltr:
    if not primes.get(int(p_ltr), False) or not primes.get(int(p_rtl), False):
      t = False
      break
    p_ltr = p_ltr[1:]
    p_rtl = p_rtl[:-1]
  if t:
    truncatable += [p]
    if len(truncatable) == 11:
      break
    
print sum(truncatable)