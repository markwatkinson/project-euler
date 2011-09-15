
"""What is the millionth lexicographic permutation of the digits
0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?"""


from lib import euler

seq = [int(c) for c in '0123456789']

permutations = []

for x in range(10**6 - 1): # -1 because the first is seq
  s = euler.lexicographic_permutation(seq)
  permutations += [s]
  seq = s

print ''.join([str(i) for i in permutations[-1]])