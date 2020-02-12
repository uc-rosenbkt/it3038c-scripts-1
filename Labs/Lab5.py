import time

print ("Please enter a word: ")
word = input()

vowels = 0
consonants = 0

for w in word:
    if (w == 'a' or w == 'e' or w == 'i' or w == 'u' or w == 'o' or w == 'A' or w == 'E' or w == 'U' or w == 'O'):
        vowels = vowels + 1
    else:
        consonants = consonants + 1

characters = (consonants + vowels)


time.sleep(1)
print ("You entered: '%s'" % word)
print ("Total characters: %s" % characters)
print ("Number of vowels: %s" % vowels)
print ("Number of consonants: %s" % consonants) 
    

