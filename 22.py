"""Score names according to their letters (a=1, b=2 ...), and position in a
list"""

import csv
names = []
reader = csv.reader(open('data/22.names.txt', 'r'))
names = [n for n in reader][0]

names.sort()


scores = []
for i, name in enumerate(names):
  scores += [(i+1) * sum( [ord(c)-ord('A') + 1 for c in name] ) ]

print sum(scores)