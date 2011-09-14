#!/usr/bin/env python

"""What is the largest prime factor of the number 600851475143 ?"""



n = 600851475143

from lib import euler

print euler.factor(n)[-1]

