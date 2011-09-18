"""
Generates the diagonals in the spiral as seen in Q28 and Q58
"""

def diagonals():
  x = 3
  last_number = 1
  while True:
    # the range is from the last number up to the layer squared.
    new_numbers = (last_number, x**2)
    range_ = new_numbers[1] - new_numbers[0]

    yield (
      (range_/4 + new_numbers[0]),
      (range_/2 + new_numbers[0]),
      (3*range_/4 + new_numbers[0]),
      (new_numbers[1])
    )
    x += 2
    last_number = new_numbers[1]


