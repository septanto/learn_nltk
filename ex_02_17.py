import nltk
from nltk.corpus import gutenberg
from nltk.corpus import stopwords

def excercise(text):
    stop_words = stopwords.words('english')
    wordsx = [w.lower() for w in text if w.isalpha()]
    fd = nltk.FreqDist(wordsx)
    for stops in stop_words:
        fd.pop(stops, 'ok')
    return fd.most_common(50)

print(excercise(gutenberg.words('austen-emma.txt')))