 

"""
http://projecteuler.net/index.php?section=problems&id=33

strange fractions
"""

a, b = 11, 1
fractions = []
while b <= 99:
  # apologies for terrible naming here. We use lists to more easily manipulate
  # the contents than strings
  b_ = list(str(b))
  for a in range(10, b):
    # check if a and b have a common number
    a_ = list(str(a))
    for n in a_:
      # exclude 0, it's either a trivial case or a division by zero
      if n == '0': continue
      if n in b_:
        a__, b__ = list(a_), list(b_)
        a__.remove(n), b__.remove(n)
        # get it back to an int
        cancelled_a, cancelled_b_ = int(''.join(a__)), int(''.join(b__))
        if cancelled_b_ == 0: continue
        if cancelled_a/float(cancelled_b_) == a/float(b):
          print a, b, 'removed', n
          fractions += [(a, b)]
  b+=1

print 'fractions are'
print '\n'.join( [str(a) + '/' + str(b) for a, b in fractions] )


product = [1, 1]
for a, b in fractions:
  product[0] *= a
  product[1] *= b

from lib import euler

# now simplify the product

while 1:
  a_divisors = euler.divisors(product[0])
  b_divisors = euler.divisors(product[1])
  brk = False
  for d in a_divisors[::-1]:
    if d in b_divisors:
      #print 'dividing by', d
      if d == 1:
        brk = True
        break
      else:
        product = [product[0]/d, product[1]/d]
        #print product
        break
  if brk:
    break

print 'Simplified product:', str(product[0]) + '/' + str(product[1])
