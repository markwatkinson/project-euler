 
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