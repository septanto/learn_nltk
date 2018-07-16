import nltk
from nltk.corpus import brown

genres = brown.categories()

cfd = nltk.ConditionalFreqDist(
    (genre, word.lower())
    for genre in genres
    for word in brown.words(categories=genre)
)

time = ['morning', 'night', 'day', 'afternoon', 'evening']
cfd.plot(conditions=genres, samples=time)