import nltk

words=nltk.corpus.brown.words(categories=['news', 'romance'])
days=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
cfd = nltk.ConditionalFreqDist((category, word) for category in ['news', 'romance'] for word in nltk.corpus.brown.words(categories=[category]))
cfd.tabulate(samples=days)
cfd.plot(samples=days)

def generate_model(cfdist, word, num=15):
    for i in range(num):
        print word,
        word=cfdist[word].max()

text = nltk.corpus.genesis.words('english-kjv.txt')
print text
bigrams=nltk.bigrams(text)
print bigrams
cfd=nltk.ConditionalFreqDist(bigrams)
print cfd

print cfd['God']
generate_model (cfd, 'God')
