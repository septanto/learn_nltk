import nltk
from nltk.corpus import gutenberg

def hedge(text):
    result = []
    for i in range(len(text)):
        if i % 3 == 0 and i > 0:
            result.append('like')
            result.append(text[i])
        else:
            result.append(text[i])
    return result

emma = gutenberg.words('austen-emma.txt')
result = hedge(emma[0:20])
print(result)