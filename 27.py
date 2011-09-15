 
"""
Considering quadratics of the form:

    n*n + an + b, where |a| < 1000 and |b| < 1000

    where |n| is the modulus/absolute value of n
    e.g. |11| = 11 and |-4| = 4

Find the product of the coefficients, a and b, for the quadratic expression
that produces the maximum number of primes for consecutive values of n,
starting with n = 0."""


# I think the naive test should be okay as long as we cache the results of
# primality tests

from lib import euler

primes = {}

def f(n, a, b):
  return n**2 + a*n + b


def test(a, b):
  n = 0
  while 1:
    term = f(n, a, b)
    p = primes.get(term, None) 
    if p is None:
      p = euler.is_prime(term)
      primes[term] = p
    if p:
      n+=1
    else: break
  return n


data = (0, 0, 0)
for a in range(-1000, 1000):
  for b in range(-1000, 1000):
    length = test(a, b)
    if length > data[2]: data = (a, b, length)

print data
print data[0] * data[1]
