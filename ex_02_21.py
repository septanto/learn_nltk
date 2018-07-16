import nltk
from nltk.corpus import cmudict
from nltk.corpus import gutenberg

dict = cmudict.dict()

def exercise(text):
    words = []
    result = 0
    exception = []
    for word in text:
        if word.isalpha():
            words.append(word.lower())
    fd = nltk.FreqDist(words)
    for word in fd:
        try:
            no_syllables = len(dict[word][0])
            freq = fd[word]
            total_syllables = no_syllables * freq
            result += total_syllables
        except KeyError:
            exception.append(word)
    print('\nWords not found in dict: ')
    print(exception)
    print('\nTotal syllables: ')
    print(result)

exercise(gutenberg.words('melville-moby_dick.txt'))