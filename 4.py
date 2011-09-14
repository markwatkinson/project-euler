#!/usr/bin/env python

"""Find the largest palindrome made from the product of two 3-digit numbers."""

from lib import euler

largest = 0
for i in xrange(100, 1000):
  for j in xrange(100, 1000):
    product = i*j
    if euler.is_palindrome(product) and product > largest:
      largest = product

print largest
