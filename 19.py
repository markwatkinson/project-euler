"""How many Sundays fell on the first of the month during the twentieth century
(1 Jan 1901 to 31 Dec 2000)?"""

# The alternative appears to grind through the years on a monthly basis,
# applying congruence relations as we go. This sounds dull so I'll use
# the time library instead.

import time

count = 0
for year in xrange(1901, 2001):
  for month in xrange(0, 12):
    tstruct = time.strptime('01 {0} {1}'.format(month+1, year), '%d %m %Y')
    if tstruct.tm_wday == 6: # sunday
      count+=1

print count