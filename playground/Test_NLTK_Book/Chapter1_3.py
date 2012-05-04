saying = 'After all is said and done more is said then done'.split()
tokens = sorted(set(saying))
print tokens [-2:]


from nltk.book import *


fdist1 = FreqDist(text1)
vocab = fdist1.keys()
print vocab[:50]

fdist1.plot(50, cumulative=True)

print fdist1.hapaxes()

V=set(text1)
long_words = [w for w in V if len(w)>15]
print sorted(long_words)


print sorted([w for w in set(text1) if len(w)>7 and fdist1[w]>7])

print bigrams (['more', 'is', 'good'])

text1.collocations()


fdist2=FreqDist([len(w) for w in text1])

#1.4:
len(set([word.lower() for word in text1 if word.isalpha()]))
