from __future__ import division
import nltk, re, pprint
from nltk.corpus import gutenberg
raw=gutenberg.raw('melville-moby_dick.txt')
fdist=nltk.FreqDist(ch.lower() for ch in raw if ch.isalpha())
fdist.plot()
