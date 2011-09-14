"""
1) a < b < c
2) a*a + b*b = c*c
3) a + b + c = 1000


find a*b*c
"""

"""

2 => sqrt(a*a + b*b) = c

sub into 3)

a + b + sqrt(a*a + b*b) = 1000

now we have only two unknowns

"""

import math

a, b = None, None

for b in range(1000, 0 ,-1):
  brk = False
  for a in range(b-1, 0, -1):
    if a + b + math.sqrt(a*a + b*b) == 1000:
      brk = True
      break
  if brk:
    break
    

c = int(math.sqrt(a*a + b*b))
assert(a + b + c) == 1000
print 'a, b, c =', a, b, c
print 'abc = ' + str(a*b*c)

