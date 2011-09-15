 
"""
What is the value of the first triangle number to have over five hundred divisors?
"""

from lib import euler

i = 1
numbers = []
while 1:
  numbers += [i]
  triangle_number = sum(numbers)
  num_divisors = euler.num_divisors(triangle_number)
  if num_divisors > 500:
    print triangle_number
    break
  i+=1
  
  