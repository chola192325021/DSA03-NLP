#exp-3

import nltk
from nltk.stem import PorterStemmer, WordNetLemmatizer

# Download WordNet data (run only once)
nltk.download('wordnet')

# Create objects
stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()

# List of words
words = list(map(str,input("Enter the words:").split()))

print("Original Words:")
print(words)

print("\nStemming:")
for word in words:
    print(word, "->", stemmer.stem(word))

print("\nLemmatization:")
for word in words:
    print(word, "->", lemmatizer.lemmatize(word))
