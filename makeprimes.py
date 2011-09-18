import atexit
from lib import euler

existing_primes = []
try:
  with open('data/primes') as f:
    l = f.read()
    existing_primes = [int(p) for p in l.splitlines()]
except IOError: pass

def write():
  global new_primes
  if new_primes:
    to_write = '\n'.join([str(n) for n in new_primes]) + '\n'
    with open('data/primes', 'a') as f:
      f.write(to_write)
  new_primes = []

i = len(existing_primes)
generator = euler.primes(i, existing_primes)
new_primes = []
while 1:
  new_primes += [generator.next()]
  if len(new_primes) > 1000: write()


