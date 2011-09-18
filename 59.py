

ciphertext = []
with open('data/59.cipher1.txt') as f:
  for char in f.read().replace(',', '\n').splitlines():
    ciphertext += [int(char)]


def decrypt(ciphertext, key):
  return ''.join( [chr(c ^ k) for c, k in zip(ciphertext, key) ] )


def analyse(plaintext):
  if ' and ' in plaintext and ' the ' in plaintext:
    return True
  return False

chars = 'abcdefghijklmnopqrstuvwxyz'

for a in chars:
  for b in chars:
    for c in chars:
      password_str = a + b + c
      key = []
      for i in range(len(ciphertext)):
        key += [ord(password_str[i % 3])]
      plaintext = decrypt(ciphertext, key)
      if analyse(plaintext):
        print plaintext
        print 'password =', password_str
        print sum( [ord(c) for c in plaintext] ) 
        