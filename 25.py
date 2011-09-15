 
"""What is the first term in the Fibonacci sequence to contain 1000 digits?"""

from lib import euler

for i, f in enumerate(euler.fibonacci()):
  #print i+1, f
  if len(str(f)) >= 1000:
    print i+1
    break
  