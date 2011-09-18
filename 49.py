

from lib import euler

primes = []
for p in euler.primes():
  if p > 9999: break
  if p > 1000: primes += [p]


for i, p in enumerate(primes):
  for j in range(i+1, len(primes)):
    p1 = primes[j]
    diff = p1 - p
    if p1 + diff in primes:
      # this is a pretty roguh check for permutations
      lsts = [list(str(x)) for x in [p, p1, p1+diff]]
      perms = True
      for s in lsts:
        s.sort()
      strs = [''.join(x) for x in lsts]
      if len(list(set(strs))) == 1:
        # there are two answers, so we'll just print whatever we find
        print p, p1, p1+diff