 
"""
find the last 10 digits of 1**1 + 2**2 ... 1000*1000

this is easy because we only need to consider the last 10 digits of each
number
"""

s = 0
for x in range(1, 1001):
  s += x**x
  s = s % 10000000000
print s