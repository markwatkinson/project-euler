from lib import euler

prime_generator = euler.primes()

for x in range(10001):
  p = prime_generator.next()
print p
