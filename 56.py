 
"""
Considering natural numbers of the form, a^b, where a, b < 100,
what is the maximum digital sum?
"""
from lib import euler
max_ = (0, 0)
for a in range(100):
  for b in range(100):
    s = euler.digital_sum(a**b)
    if s > max_[1]: max_ = (a**b, s)
print max_[1]