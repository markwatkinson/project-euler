"""
What is the largest n-digit pandigital prime that exists?
"""



from lib import euler
import math

digits = '0123456789'

while digits:

  n = digits
  print n
  p = 0
  while 1:
    if int(n) > p and euler.is_prime(int(n)):
      p = int(n)
    try:
      n = ''.join(euler.lexicographic_permutation(n))
    except: break
  if p: break
  
  digits = digits[:-1]
  
print p