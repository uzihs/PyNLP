from __future__ import division
import nltk, re, pprint
wordlist = [w for w in nltk.corpus.words.words('en') if w.islower()]
print [w for w in wordlist if re.search('ery$',w)]

#T9 (keypad)
print [w for w in wordlist if re.search('^[ghi][mno][jlk][def]$', w)]
