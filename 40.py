"""
Basically, the Q is to concatenate all the numbers to find the
product of the indices at powers of 10 up to 7,
"""
n = ''
i = 1
while True:
  n += str(i)
  if len(n) > 10*10**6: break
  i+=1

product = 1
for x in range(7):
  product *= int(n[10**x-1])
print product
  
