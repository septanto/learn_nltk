import nltk
from nltk.corpus import brown

def lexical_diversity(corpus):
    ld = [' ']
    for genre in corpus.categories():
        ld.append(len(corpus.words(categories=genre))/len(set(corpus.words(categories=genre))))

    cfd = nltk.ConditionalFreqDist(
        (genre_name, genre_count)
        for genre_name in corpus.categories()
        for genre_count in ld
    )

    return cfd.plot()

# def ldt(corpus):
#     cfd = nltk.ConditionalFreqDist(
#         (genre, len(corpus.words(categories=genre))/len(set(corpus.words(categories=genre))))
#         for genre in corpus.categories()
#     )

#     return cfd.tabulate()

# def ld(corpus):
#     for genre in corpus.categories():
#         ld = len(corpus.words(categories=genre))/len(set(corpus.words(categories=genre)))
#         print(genre + ':', ld)
#     return 0

lexical_diversity(brown)