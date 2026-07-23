#EXP-8

import random

probability_tags = {
    "I": ["PRP"],
    "you": ["PRP"],
    "eat": ["VB"],
    "apple": ["NN"],
    "mango": ["NN"],
    "quickly": ["RB"],
    "beautiful": ["JJ"],
    "the": ["DT"],
    "a": ["DT"]
}

sentence = input("Enter a sentence: ")

words = sentence.split()

tagged = []

for word in words:
    if word in probability_tags:
        tag = random.choice(probability_tags[word])
    else:
        tag = "NN"

    tagged.append((word, tag))

print("\nTagged Sentence:\n")

for word, tag in tagged:
    print(word, "->", tag)
