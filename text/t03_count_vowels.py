from sys import argv

script, filename = argv

def count_vowels():
  vowels = {'a':0, 'e':0, 'i':0, 'o':0, 'u':0, 'y':0}
  with open(filename, 'r') as f:
    data = f.read()
  for char in data:
    if char.lower() in vowels:
      vowels[char]+=1

  print 'There are {} vowels in text file {}'.format(sum(vowels.itervalues()), filename) 
  for vowel in vowels:
    print '{} occurs {} times'.format(vowel, vowels[vowel])
  
count_vowels()