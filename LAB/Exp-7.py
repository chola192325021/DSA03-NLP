#EXP-7

import nltk
from nltk.tokenize import word_tokenize
from nltk import pos_tag

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger_eng')

text = input("Enter a sentence: ")

words = word_tokenize(text)

tagged_words = pos_tag(words)

print("\nPOS Tagged Words:\n")

for word, tag in tagged_words:
    print(word, "->", tag)
