 
"""
Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.
"""

from lib import euler

# seems easy enough...


def to_binary(n):
  s = ''
  if n == 0: return '0'
  while n:
    s += '1' if n % 2 else '0'
    n = n >> 1
  return s[::-1]

palindromes = []
for i in xrange(10**6):
  if euler.is_palindrome(i) and euler.is_palindrome(to_binary(i)):
    palindromes += [i]

print sum(palindromes)

