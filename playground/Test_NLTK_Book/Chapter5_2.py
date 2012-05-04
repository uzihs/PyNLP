pos = {'colorless': 'ADJ', 'ideas': 'N', 'sleep': 'V', 'furiously': 'ADV'}
list(pos)
sorted(pos)
[w for w in pos if w.endswith('s')]

pos.keys()
pos.values()
pos.items()

for key, val in sorted(pos.items()): 
     print key + ":", val

frequency = nltk.defaultdict(int)
frequency['ideas'] #returns 0 (adds it?)

pos = nltk.defaultdict(lambda: 'N')
pos['blog'] #returns 'N' (adds it?)


alice = nltk.corpus.gutenberg.words('carroll-alice.txt')
vocab = nltk.FreqDist(alice)
v1000 = list(vocab)[:1000]
mapping = nltk.defaultdict(lambda: 'UNK')
for v in v1000:
    mapping[v] = v

alice2 = [mapping[v] for v in alice]
alice2[:100]

#not from the book - the standard python for default dict (from Python 2.5)
import collections
d=collections.defaultdict(int)
d[1] #returns 0


pair=('NP', 32)
from operator import itemgetter
itemgetter(1)(pair) #equivelant to pair[1]

counts = nltk.defaultdict(int)
from nltk.corpus import brown
for (word, tag) in brown.tagged_words(categories='news'):
    counts[tag] += 1
list(counts)
from operator import itemgetter
sorted(counts.items(), key=itemgetter(1), reverse=True)
[t for t, c in sorted(counts.items(), key=itemgetter(1), reverse=True)]


last_letters = nltk.defaultdict(list)
words = nltk.corpus.words.words('en')
for word in words:
    key = word[-2:]
    last_letters[key].append(word)
last_letters['ly']


anagrams = nltk.defaultdict(list)
for word in words:
    key = ''.join(sorted(word))
    anagrams[key].append(word)
anagrams['aeilnrt']


pos = nltk.defaultdict(lambda: nltk.defaultdict(int))
brown_news_tagged = brown.tagged_words(categories='news', simplify_tags=True)
for ((w1, t1), (w2, t2)) in nltk.ibigrams(brown_news_tagged): 
    pos[(t1, w2)][t2] += 1 
pos[('DET', 'right')]


counts = nltk.defaultdict(int)
for word in nltk.corpus.gutenberg.words('milton-paradise.txt'):
    counts[word] += 1
[key for (key, value) in counts.items() if value == 32]


pos = {'colorless': 'ADJ', 'ideas': 'N', 'sleep': 'V', 'furiously': 'ADV'}
pos2 = dict((value, key) for (key, value) in pos.items())
pos2['N']

pos.update({'cats': 'N', 'scratch': 'V', 'peacefully': 'ADV', 'old': 'ADJ'})
pos2 = nltk.defaultdict(list)
for key, value in pos.items():
    pos2[value].append(key)
pos2['ADV']

pos2 = nltk.Index((value, key) for (key, value) in pos.items())
pos2['ADV']
