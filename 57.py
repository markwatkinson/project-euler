"""
In the first one-thousand expansions of sqrt(2), how many fractions contain a
numerator with more digits than denominator?
"""


# I hate programming with fractions

def series(n):
  # the series is:
  # sqrt(2) = 1 + 1/(2 + 1/(2 + ... ))
  # we're starting off in the middle and working outwards.
  # the middle is always 1/2.
  # each term adds 2 then divides 1 by the result.
  # then we end up at the start, which adds 1
  fraction = [1, 2]
  for i in range(n):
    fraction[0] += 2*fraction[1]
    # 1 / (a/b) =  b/a
    fraction = [fraction[1], fraction[0]]
    
  fraction[0] += fraction[1]
  return fraction

s = 0
for x in range(1000):
  fraction = series(x)
  if len(str(fraction[0])) > len(str(fraction[1])):
    s += 1
print s
