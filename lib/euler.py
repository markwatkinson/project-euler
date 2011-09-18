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

def integers(n=0, step=1):
  """ Generates a list of integers like xrange, but with no upper boind.
  Slightly neater than messing around with while loops and counters """
  while 1:
    yield n
    n += step

def is_prime(n):
  if n != 2 and n % 2 == 0: return False
  if n != 3 and n % 3 == 0: return False
  if n != 5 and n % 5 == 0: return False
  if n != 7 and n % 7 == 0: return False
  return len(divisors(n)) == 2

def divisors(n):
  """ returns a list of the divisors that divide into n (including 1 and itself)
  warning: slow """
  divisors = []
  for i in xrange(1, int(math.sqrt(n))+1, 2 if n%2 else 1):
    if n % i == 0: divisors += [i, n/i]
  divisors = list(set(divisors))
  divisors.sort()
  return divisors

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


def primes(i=2, primes=[]):
  """ Generates prime numbers indefnitely """
  i = max(2, i)
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


def lexicographic_permutation(seq):
  """ BUG: I hacked this together quickly and it always returns a list
  even if the input was a string.
  I don't want to change it for compat reasons
  """
  # http://en.wikipedia.org/wiki/Permutation#Systematic_generation_of_all_permutations
  k = None
  for i in range(len(seq)-1)[::-1]:
    if seq[i] < seq[i+1]:
      k = i
      break
  if k is None: raise Exception('no more permutations')

  l = None
  for i in range(len(seq))[::-1]:
    if seq[k] < seq[i]:
      l = i
      break
  assert l is not None
  new_seq = [s for s in seq]
  tmp = seq[k]
  new_seq[k] = seq[l]
  new_seq[l] = tmp
  new_seq = new_seq[:k+1] + new_seq[k+1:][::-1]
  return new_seq

def permutate(seq):
  is_str = isinstance(seq, str)
  yield seq
  while 1:
    try:
      seq = lexicographic_permutation(seq)
      if is_str: seq = ''.join(seq)
      yield seq
    except:
      break

def fibonacci():
  """ generates the fibonacci sequence indefinitely """
  a, b = 1, 1
  yield a
  yield b
  while 1:
    a, b = b, a+b
    yield b



def quadratic(a, b, c):
  try: 
    determinant = math.sqrt( b**2 - 4*a*c )
  except: return None
  return ((-b + determinant)/(2*a), (-b - determinant)/(2*a))


def triangular_numbers(n=1):
  while 1:
    yield n*(n+1)/2
    n += 1

def is_triangle(n):
  """ Return true if a number is triangular"""
  if n != int(n) or n < 1: return False
  # T = n(n+1)/2
  # n**2 - n - 2*T = 0
  s = quadratic(1, -1, -2*n)
  if s is None: return False
  for soln in s:
    if soln >= 1 and int(soln) == soln: return True
  return False

def is_hexagonal(n):
  """ Return true if a number is hexagonal"""
  if n != int(n) or n < 1: return False
  # H = n(2n-1)
  # 2n**2 - n - H = 0
  s = quadratic(2, -1, -1*n)
  if s is None: return False
  for soln in s:
    if soln >= 1 and int(soln) == soln: return True
  return False

def is_pentagonal(p):
  """ Return true if a number is pentagonal"""
  if p != int(p) or p < 1: return False
  # p = n(3n-1)/2
  # we need to see if there exists a real integer solution for n given that we
  # know p
  # 2p = n(3n-1)
  # 2p = 3n**2 - n
  # 3n**2 - n - 2p = 0
  # quadratic in n
  n = quadratic(3, -1, -2*p)
  if n is None: return False
  #print n
  for soln in n:
    if soln >= 1 and int(soln) == soln:
      return True
  return False



def combination(n, r):
  return math.factorial(n) / (math.factorial(r)*math.factorial(n-r))

def digital_sum(n):
  return sum( [int(x) for x in str(n) ] )