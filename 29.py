 
"""
  calculate how many distinct terms there are for a**b for 2<=a<=100, 2<=b<=100
"""

# seems... easy

results = []
for a in xrange(2, 101):
  for b in xrange(2, 101):
    results += [a**b]

print len(list(set(results)))