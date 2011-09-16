 
"""
How many different ways can 2 pounds be made using any number of coins?
"""

"""

1 : 1   
2:  2    
5:  4   
10: 11



2p:

1 2p
2 1p

5p

1 5p
2 2p 1 1p
1 2p 3 1p
5 1p


10p:

1 10p
2 5p
1 5p 2 2p 1 1p
1 5p 1 2p 2 1p
1 5p 5 1p
5 2p
4 2p 2 1p
3 2p 4 1p
2 2p 6 1p
1 2p 8 1p
10 1p


20p:
1 20p
2 10p
1 10p ....  [11]





"""


coins = [1, 2, 5, 10, 20, 50, 100, 200]

# iterate over the coins, then over the individual values up to 200
w = [1] + [0 for x in xrange(200)] 
for c in coins:
  for i in xrange(c, 201):
    # the number of ways a value can be made is a sum of some of the`
    # coins below it, i.e. for 200 we need to check 199, 198, 195, 190, 180,
    # 150, and 100, as that encompasses 1, 2, 5, 10, 20, 50, and 100p
    w[i] += w[i-c]

print w[-1]