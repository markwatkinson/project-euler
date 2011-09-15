
""" If all the numbers from 1 to 1000 (one thousand) inclusive were written
out in words, how many letters would be used?
"""


# this question is a pain
WORDS = {
  'digits': [None, 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight',
    'nine', 'ten',
    # inconsistent
    'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen',
  'eighteen', 'nineteen'],
  'tens': [
    None,
    None,
    'twenty',
    'thirty',
    'forty',
    'fifty',
    'sixty',
    'seventy',
    'eighty',
    'ninety',
  ]
}



def make_word(number):

  # first do the 10s
  # the array will be backwards
  words = []
  tens = number % 100
  if 0 < tens < 20:
    words += [WORDS['digits'][tens]]
  elif tens >= 20:
    digit = number % 10
    if digit: words += [WORDS['digits'][digit]]
    words += [WORDS['tens'][tens/10]]
  # now hundreds
  hundreds = (number % 1000) / 100
  if hundreds:
    if tens:
      words += ['and']
    words += ['hundred']
    words += [WORDS['digits'][hundreds]]
    
  if number == 1000:
    words += ['thousand']
    words += ['one']
  return words[::-1]

letters = []
for x in range(1, 1001):
  words = make_word(x)
  letters += [sum([len(w) for w in words])]
  #print letters, words
print sum(letters)