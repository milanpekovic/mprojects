from sys import argv

script, word = argv
vowels = 'aeiou'

def pig_latin(s):
    s = s.lower()
    if s[0] in vowels:
        return s.capitalize() + 'ay'
    else:
        return s[1:].capitalize() + s[0] + 'ay'

print pig_latin(word)
    
