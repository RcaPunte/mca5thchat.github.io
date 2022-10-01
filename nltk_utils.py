import numpy as np
import nltk
# nltk.download('punkt')
from nltk.stem.porter import PorterStemmer
stemmer = PorterStemmer()

# 1. conda activate env
# 2. pip install nltk

# Sentence atang word then hran
# a="How long does shipping take?"
# print(a)
# a=tokenize(a)
# print(a)


def tokenize(sentence):
    """
    split sentence into array of words/tokens
    a token can be a word or punctuation character, or number
    """
    return nltk.word_tokenize(sentence)
# Word root word a dah
# words=["organize", "organizes","organizing"]
# steam_words=[stem(w)for w in words]
# print(steam_words)


def stem(word):
    """
    steamming = find the root from of the word
    examples:
    words=["organize","organizes","organizing"]
    words = [stem(w) for w in words]
    ->["organ","organ","organ"]
    """
    return stemmer.stem(word.lower())
#


def bag_of_words(tokenized_sentence, words):
    """
    sentence= ["hello", "how","are","you"]
    words = ["hi","hello","i","you","bye","thanl","cool"]
    bag = [0,1,0,1,0,0,0] 
    """
    sentence_words = [stem(word)for word in tokenized_sentence]
    bag = np.zeros(len(words), dtype=np.float32)
    for idx, w in enumerate(words):
        if w in sentence_words:  # tokenized_sentence:
            bag[idx] = 1
    return bag

#

# words=["organize", "organizes","organizing"]
# stem_words=[stem(w)for w in words]
# print(stem_words)
