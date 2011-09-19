"""
http://projecteuler.net/index.php?section=problems&id=61
"""
import sys
from lib import euler


def is_cyclic(a, b):
  return str(a)[-2:] == str(b)[:2]

generators = (
  euler.triangular_numbers(),
  euler.square_numbers(),
  euler.pentagonal_numbers(),
  euler.hexagonal_numbers(),
  euler.heptagonal_numbers(),
  euler.octagonal_numbers()
)

# we're told in the Q we only need to consider 4 digit numbers

numbers = []
for g in generators:

  nums = []
  for number in g:
    if len(str(number)) < 4: continue
    if len(str(number)) > 4: break
    nums += [number]
  numbers += [nums]

# I think since the order is undefined, we need to use recursion
# and deal with a possibility tree
# we'll use the current 'branch' and the remaining set of triangular, square,
# etcs as arguments
# we'll write to a global var instead of returning stuff otherwise
# determining the minimum sum gets very confusing because we have to return
# sets then somewhere consider all the sets

ans = None
def solve(branch, numbers):
  global ans
  if len(branch) == 6:
    if is_cyclic(branch[-1], branch[0]):
      if ans is None or sum(branch) < ans:
        ans = sum(branch)
    return

  assert numbers

  for i, nums in enumerate(numbers):
    sliced = numbers[:i] + numbers[i+1:]
    for n in nums:
      if not branch: solve([n], sliced)
      elif is_cyclic(branch[-1], n): solve(branch + [n], sliced)


solve([], numbers)
print ans
