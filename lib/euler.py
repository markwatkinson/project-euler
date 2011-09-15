import math

def factor(n):
  """ Returns the prime factors of a number """
  a = 2
  factors = []
  while n > 1:
    while (n % a == 0):
      factors += [a]
      n /= a
    a+=1
  return factors

def num_divisors(n):
  """ Returns the number of divisors of a number """
  # special case
  if n < 1: raise Exception("num_divisors called with {0}".format(n))
  if n == 1: return 1

  # if memory serves, the way to do this is to take the prime factors
  # and look at how many times each is repeated. Add 1 to each power, then
  # multiply the results
  
  factors = factor(n)
  powers = []  
  for f in set(factors): # unique
    powers += [factors.count(f)]
  
  powers = [1+p for p in powers]  
  return product(powers)
    

def is_palindrome(n):
  """ Returns true if a number is palindromic, else false """
  s = str(n)
  return s == s[::-1]

def sum_of_squares(seq):
  """Calculates the sum of squares of the sequence"""
  return sum(map(lambda x: x*x, seq))

def square_of_sum(seq):
  """Calculates the square of the sum of the sequence"""
  return sum(seq)**2


def primes():
  """ Generates prime numbers indefnitely """
  i = 2
  primes = []
  while 1:
    prime = True
    limit = int(math.sqrt(i))
    for p in primes:
      if p > limit: break
      if i % p == 0:
        prime = False
        break
    if prime:
      primes += [i]
      yield i
    i+=1


def product(seq):
  return reduce(lambda a, b: a*b, seq)