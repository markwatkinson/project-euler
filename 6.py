"""Find the difference between the sum of the squares of the first one hundred
natural numbers and the square of the sum."""

from lib import euler

seq = range(1, 101)
print abs(euler.sum_of_squares(seq) - euler.square_of_sum(seq))
