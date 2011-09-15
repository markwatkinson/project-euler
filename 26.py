 
"""
Find the value of d < 1000 for which 1/d contains the longest recurring cycle
in its decimal fraction part.

"""

# http://mathworld.wolfram.com/DecimalExpansion.html has some info on this

from lib import euler

def cycle_length(n):
  # we need to solve 10**s = 10**(s+t)  (mod n)

  # does this always halt?
  cycles = []
  i = 0
  s, t = None, None
  while 1:
    x = 10**i % n
    if x in cycles:
      s = cycles.index(x)
      t = i - s
      break
    cycles += [x]
    i+=1
  
  return t

data = (0, 0)
for x in range(1, 1000):
  cycles = cycle_length(x)
  if cycles > data[1]: data = (x, cycles)
print data