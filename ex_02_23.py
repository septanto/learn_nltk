import nltk
import matplotlib.pyplot as plt
from nltk.corpus import gutenberg

words = []

for word in gutenberg.words('shakespeare-hamlet.txt'):
    if word.isalpha():
        words.append(word.lower())

fd = nltk.FreqDist(words)

freq_list = sorted(list(fd.values()), reverse=True)

plt.plot(freq_list)
plt.ylabel('Fequency')
plt.show()