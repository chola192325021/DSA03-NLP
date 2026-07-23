#EXP-6

import random
import nltk
from nltk.util import bigrams

nltk.download('punkt_tab')

text = """
Natural language processing is interesting.
Natural language processing is useful.
Natural language understanding is important.
"""

tokens = nltk.word_tokenize(text)

bg = list(bigrams(tokens))

bigram_dict = {}

for w1, w2 in bg:
    if w1 not in bigram_dict:
        bigram_dict[w1] = []
    bigram_dict[w1].append(w2)

current_word = "Natural"
generated = [current_word]

for i in range(5):
    if current_word in bigram_dict:
        next_word = random.choice(bigram_dict[current_word])
        generated.append(next_word)
        current_word = next_word
    else:
        break

print("Generated Text:")
print(" ".join(generated))
