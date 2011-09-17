 
"""
A triangle number is 1/2 * n(n+1) for integer n >=1

A triangle word is a word whose letters sum to a triangle number
(a = 1, b = 2 etc)

In the given word list, how many are triangle words?
"""

import csv
reader = csv.reader(open('data/42.words.txt'))
words = [w for w in reader][0]

# generate a list of sums corresponding to the words, 
sums = []
for word in words:
  sums += [sum( [ord(c) - ord('A') + 1 for c in word] )]
max_ = max(sums)
# then generate triangle numbers up to the maximum sum, and see how many
# times each triangle number features in the sum list
n = 1
t =  1
total = 0
while t < max_:
  total += sums.count(t)
  n += 1
  t = int(0.5 * n * (n + 1))

print total