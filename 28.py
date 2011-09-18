 
""" confusing spiral patterns, read the description on the site

http://projecteuler.net/index.php?section=problems&id=28

"""
# the key to this one is to generate the diagonals, not the whole
# spiral. It's not that hard if you notice each additional layer adds a
# range of numbers, and the diagonals are situated at the 1/4, 1/2, 3/4, 1
# parts of the range.

from lib import spiraldiagonals



diagonals = [1]
last_number = 1

generator = spiraldiagonals.diagonals()

for x in range(3, 1002, 2):
  ds = generator.next()
  diagonals += [d for d in ds]

print sum(diagonals)
