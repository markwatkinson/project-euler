 
""" confusing spiral patterns, read the description on the site

http://projecteuler.net/index.php?section=problems&id=28

"""
# the key to this one is to generate the diagonals, not the whole
# spiral. It's not that hard if you notice each additional layer adds a
# range of numbers, and the diagonals are situated at the 1/4, 1/2, 3/4, 1
# parts of the range.


diagonals = [1]
last_number = 1

for x in range(3, 1002, 2):
  # the range is from the last number up to the layer squared.
  new_numbers = (last_number, x**2)
  range_ = new_numbers[1] - new_numbers[0]

  diagonals += [
    (range_/4 + new_numbers[0]),
    (range_/2 + new_numbers[0]),
    (3*range_/4 + new_numbers[0]),
    (new_numbers[1])
  ]

  last_number = new_numbers[1]

print sum(diagonals)
