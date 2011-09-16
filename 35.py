 
"""
How many circular primes are there below one million?
a circular prime is a prime for which each rotation of its digits is also
prime
"""

from lib import euler

def rotate(n):
  n_ = str(n)
  return int( n_[1:] + n_[0] )

# the best way to do this is to generate a list of primes below 1m then
# iterate over it, rotating it as we go, and elimating the items which have
# non-prime rotations.


primes = []
circular_primes = []
for p in euler.primes():
  if p >= 10**6: break
  primes += [p]

# we can quickly elimate any number which has any even digit, as at least
# one of its rotations will not be prime
def filter_func(p):
  # special case
  if p == 2: return True
  s = str(p)
  for digit in ['0', '2', '4', '6', '8']:
    if digit in s:
      return False
  return True

primes = filter(filter_func, primes)

# we need fast lookup
primes_map = {}
for p in primes:
  primes_map[p] = True


print 'generated prime list'


for p in primes_map:
  p_ = p
  prime = True
  for i in range(len(str(p))-1):
    p_ = rotate(p_)
    if not primes_map.get(p_, False):
      prime = False
      break
  if prime: circular_primes += [p]

print len(circular_primes)

# that was harder than I expected