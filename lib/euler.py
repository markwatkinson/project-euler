 
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

def is_palindrome(n):
  """ Returns true if a number is palindromic, else false """
  s = str(n)
  return s == s[::-1]