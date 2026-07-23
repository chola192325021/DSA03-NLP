#EXP-9

import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import RegexpTagger

nltk.download('punkt')

patterns = [
    (r'.*ing$', 'VBG'),
    (r'.*ed$', 'VBD'),
    (r'.*es$', 'VBZ'),
    (r'.*ly$', 'RB'),
    (r'.*ous$', 'JJ'),
    (r'.*able$', 'JJ'),
    (r'.*s$', 'NNS'),
    (r'^[Tt]he$', 'DT'),
    (r'^[Aa]$', 'DT'),
    (r'^[Aa]n$', 'DT'),
    (r'.*', 'NN')
]

tagger = RegexpTagger(patterns)

text = input("Enter a sentence: ")

tokens = word_tokenize(text)

tagged = tagger.tag(tokens)

print("\nRule-Based POS Tags:\n")

for word, tag in tagged:
    print(word, "->", tag)
