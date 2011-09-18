 
"""
Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x,
contain the same digits.
"""

# very easy once we have a neat way to check the digits of two numbers

from lib import euler


def have_same_digits(a, b):
  a_, b_ = str(a), str(b)
  if len(a_) != len(b_): return False
  a_map, b_map = {}, {}
  for n1, n2 in zip(a_, b_):
    a_map[n1] = 1 + a_map.get(n1, 0)
    b_map[n2] = 1 + b_map.get(n2, 0)
  return a_map == b_map


for x in euler.integers(2):
  same = True
  for m in xrange(2, 6):
    if not have_same_digits(x, x*m):
      same = False
      break
  if not same: continue
  print x
  break
    