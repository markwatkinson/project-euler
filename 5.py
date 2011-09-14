 
"""What is the smallest positive number that is evenly divisible by all
of the numbers from 1 to 20?"""


i = 20
range_ = range(2, 21)
while True:
  divisible = True
  for x in range_:
    if i % x != 0:
      divisible = False
      break
  if divisible:
    print i
    break
  else:
    # we can skip in blocks of 20 since it must be divisible by 20
    i+=20