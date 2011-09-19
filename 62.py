"""
Find the smallest cube for which exactly five permutations of its digits
are cube.
"""


"""
this is easy if you look at it right, and incredibly hard if you don't.
Instead of generating permutations, generate a list of cubes and count the
digits in each. Make a list of the digit counts, and see which is the first
count to occur more than five times. The index of that count will correspond
to the cube in the same index.

We don't know the upper bound, so we'll just choose something big
"""

cubes = [] # list of cubes
digits = [] # list of digit counts
n = 1
# generate the cubes
while 1:
  c = n**3
  if c > 999999999999: break
  cubes += [c]
  n += 1
# count the digits, store the count as a dict
for c in cubes:
  ds = {}
  for d in str(c):
    d = int(d)
    ds[d] = ds.get(d, 0) + 1
  digits += [ds]
# now see if any counts occur five times
for i, d in enumerate(digits):
  if digits.count(d) == 5:
    print cubes[i]
    break
