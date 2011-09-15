 
"""
Find the sum of all the numbers that can be written as the sum of fifth powers
of their digits."""

# the upper bound is going to be, hmm, 9**5 for each digit
# so an n digit number should be less than n*9**5
# so I think it can't get above 6 digits
i = 2
s_ = 0
for i in xrange(2, 6 * 9**5):
  digits = [int(n) for n in str(i)]
  powers = [n**5 for n in digits]
  s = sum(powers)
  if s == i:
    s_ += i
    print i, s_
