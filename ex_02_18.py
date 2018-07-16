import nltk
from nltk.corpus import gutenberg
from nltk.corpus import stopwords

def exercise(text):
    stop_words = stopwords.words('english')
    word_bigrams = list(nltk.bigrams(text))
    clean_bigrams = []
    for first in word_bigrams:
        clean = True
        for second in first:
            for stopword in stop_words:
                if second == stopword or second.isalpha() == False:
                    clean = False
        if clean:
            clean_bigrams.append(first)
    fd = nltk.FreqDist(clean_bigrams)
    return fd.most_common(50)

print(exercise(gutenberg.words('austen-emma.txt')))