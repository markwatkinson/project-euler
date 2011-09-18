 
"""
http://projecteuler.net/index.php?section=problems&id=55
"""

from lib import euler

# we could cache the lychrel numbers but for only 10k, we hardly need to

def is_lychrel(n, i=0):
  if i > 50: return True
  reverse = int(str(n)[::-1])
  s = n + reverse
  if euler.is_palindrome(s): return False
  else: return is_lychrel(s, i+1)

s = 0
for x in xrange(1, 10000):
  if is_lychrel(x): s+=1
print s