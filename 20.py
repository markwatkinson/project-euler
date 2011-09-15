from lib import euler

factorial_100 = euler.product(range(1, 101))
print sum([int(x) for x in str(factorial_100)])
