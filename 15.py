""" starting in the top left of a grid, how many routes are there to the
bottom right?"""


""" an interesting way to look at this is the number of routes, r() to any particular
point (a, b) = r(a, b-1) + r(a-1, b).

Start at the bottom right and recurse?

keep a cache too or we'll be here forever
"""


cache = {}

def paths(a, b):
  # base case, the origin point, 0 ways to reach this - we start there
  if a + b == 0: return 0
  # base case, a b = 0, 1 or 1, 0 - 1 way to reach this - the origin
  if a + b == 1: return 1  
  # at the edge - 1 way to reach this
  elif a == 0 or b == 0: return 1
  else:
    if cache.get((a, b), 0) != 0: return cache.get((a, b))
    p = paths(a-1, b) + paths(a, b-1)
    cache[(a, b)] = p
    return p


print paths(20, 20)

