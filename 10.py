"""Find the sum of all the primes below two million."""

from lib import euler

primes = euler.primes()
s = 0
for p in primes:
  if p >= 2*10**6: break
  s += p
print s
