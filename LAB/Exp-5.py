#exp-5

from nltk.stem import PorterStemmer

# Create Porter Stemmer object
stemmer = PorterStemmer()

# List of words
words = list(map(str,input("Enter the words:").split()))

print("Original Words:")
print(words)

print("\nStemmed Words:")
for word in words:
    print(word, "->", stemmer.stem(word))
