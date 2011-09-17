""" Find the next triangular number which is pentagonal and hexagonal, after
40755 (T_285) """
from lib import euler

# very easy with a few helpers
for t in euler.triangular_numbers(286):
  if euler.is_pentagonal(t) and euler.is_hexagonal(t):
    print t
    break