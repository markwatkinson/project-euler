"""
What is the largest 1 to 9 pandigital 9-digit number that can be formed as the
concatenated product of an integer with (1,2, ... , n) where n > 1?
"""
biggest = 0
# this upper limit is very permissive, it should probably be a lot lower
for a in xrange(100, 987654321/2):
  num_digits = 0
  numbers = []
  for b in xrange(1, 10):
    n = b*a
    num_digits +=  len(str(n))
    numbers += [n]
    if num_digits >= 9: break

  if num_digits > 9: continue
  digits = [0] * 9
  skip = False
  for n in numbers:
    for d in str(n):
      d = int(d)
      digits[d-1] += 1
      if digits[d-1] > 1: break
  
  skip = False
  for d in digits:
    if d != 1:
      skip = True
      break
  #print numbers
  #print digits
  if skip: continue

  #if we get to here the number is pangidital
  number = int( ''.join( [ str(n) for n in numbers ] ) )
  biggest = max(biggest, number)

  print a, biggest

    


