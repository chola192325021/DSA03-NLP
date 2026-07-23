#EXP-10

sentence = input("Enter a sentence: ")

words = sentence.split()

tags = []

for word in words:
    if word.endswith("ing"):
        tag = "VBG"
    else:
        tag = "NN"

    tags.append([word, tag])



for i in range(1, len(tags)):

    if tags[i-1][0].lower() == "to":
        tags[i][1] = "VB"


    if tags[i][0] == "I":
        tags[i][1] = "PRP"


if tags[0][0] == "I":
    tags[0][1] = "PRP"

print("\nTransformation-Based POS Tags:\n")

for word, tag in tags:
    print(word, "->", tag)
