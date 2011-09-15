
from lib import euler


"""Find the sum of all the positive integers which cannot be written as the
sum of two abundant numbers."""

# the q tells us that 28123 is the upper bound we need to care about
# it seems the easiest way might be to collect all abundant numbers up to
# that number and then see what numbers we can't make

def is_abundant(n):
  # special case
  if n<=1: return False
  divisors = euler.divisors(n)[:-1]
  return sum(divisors) > n


abundants = filter(lambda x: is_abundant(x), range(1, 28123))


# build the numbers list as an array of index => index, then zero the
# element when we manage to create it 

numbers = [x for x in range(0, 28123)]

for i, a in enumerate(abundants):
  brk = False
  for b in abundants:
    s = a+b
    if s >= 28123: break
    numbers[a+b] = 0

# then add the array and what should be left is the ones we couldn't create

print sum(numbers)